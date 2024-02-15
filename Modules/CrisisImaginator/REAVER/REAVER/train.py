
import numpy as np

import os
from dataloaders import get_dataloaders
from spectogram import compute_log_mel_spectrograms
from model import REAVER
import torch
import torch.nn as nn

train_loader, dev_loader = get_dataloaders() # Load the data

model = REAVER(phases="PSN", norm="std") # Load the model
#model.cuda();

learning_rate = 0.00001
epochs = 100

optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
loss_fn = nn.BCELoss()


def train_loop(dataloader, epoch,next_save_point, start_index):
    
       
    for batch_id, batch in enumerate(dataloader, start=start_index):

        size = len(dataloader.dataset) * batch['X'].shape[1]

        
        batch['X'] = batch['X'].reshape(-1,3,400)
        batch['y'] = batch['y'].reshape(-1,3,400)

        pred_p, pred_s = model(torch.tensor(compute_log_mel_spectrograms(batch["X"])))
        loss_p = loss_fn(pred_p.float(), batch["y"][:,0,:].float())
        loss_s = loss_fn(pred_s.float(), batch["y"][:,1,:].float())
        loss = loss_p + loss_s
        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch_id % 5 == 0:
            loss, current = loss.item(), batch_id * batch["X"].shape[0]
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

        current = batch_id * len(batch["X"])
        if current >= next_save_point:
            model_path = os.path.join("SlidingWindow_UnetAttn_400", f"model_epoch_{epoch}_iter_{current}.pth")
            torch.save(model.state_dict(), model_path)
            print(f"Saved model at iteration {current} to {model_path}")

            # Update the next save point
            next_save_point += 500000
        if current > size:
            break



def train_model(train_dataloader, test_dataloader, num_epochs):
    # Create a directory for saving model checkpoints
    model_save_dir = "SlidingWindow_UnetAttn_400"
    os.makedirs(model_save_dir, exist_ok=True)

    for epoch in range(num_epochs):
        print(f"Epoch {epoch+1}\n-------------------------------")
        train_loop(train_dataloader, epoch,500000, 0)



train_model(train_loader, dev_loader, num_epochs=epochs)










