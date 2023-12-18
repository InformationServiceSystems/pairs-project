from transformers import pipeline
import logging as log

log.basicConfig(level=log.DEBUG)

# loading roberta model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
# classifier = pipeline("zero-shot-classification", model="Sahajtomar/German_Zeroshot")
#classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli", device=0)


# category_labels = ['Produkt', 'Service', 'Unternehmerische', 'Verantwortung', 'Alleinstellungsmerkmale',
#                    'Verkaufskanäle', 'CRM', 'Kundenbeziehung', 'Preisgestaltung', 'Zahlungsmethoden', 'Qualität']
sentiment_labels = ['positiv', 'negativ', 'neutral']


class RobertaClassification:
    def roberta_classifier(self, text, categories_to_clasify, threshold=0.85):
        """

        :param threshold: threshold for score of classification
        :param sentence: sentence from the review to classify
        :type sentence: String
        :param review: Full review
        :type review: String

        """
        confidence_scores = {}
        # top3_category_ids = {}
        # top3_category_ids = {"sentiment": 'neutral', "Present alert": 0.0, "Past alert": 0.0, "Future alert": 0.0, "Others": 0.0}

        # top3_category_ids = {"sentiment": 'neutral', "High Alert": 0.0, "Medium Alert": 0.0, "Low Alert": 0.0, "Others": 0.0}


        # sentiment_classification = classifier(sentence, sentiment_labels, multi_label=False)
        # top1_score = sentiment_classification['scores'][0]
        # top3_category_ids['sentiment'] = 'neutral' if top1_score < threshold else sentiment_classification['labels'][0]

        bmc_classification = classifier(text, categories_to_clasify, multi_label=False)

        for idx, label in enumerate(bmc_classification['labels']):
            confidence_scores[label] = bmc_classification['scores'][idx]

        return confidence_scores



        # top3_category_ids[bmc_classification['labels'][0]] = bmc_classification['scores'][0]
        # top3_category_ids[bmc_classification['labels'][1]] = bmc_classification['scores'][1]
        # top3_category_ids[bmc_classification['labels'][2]] = bmc_classification['scores'][2]
        # top3_category_ids[bmc_classification['labels'][3]] = bmc_classification['scores'][3]
        # remove below 2 lines for PO
        #top3_category_ids[bmc_classification['labels'][5]] = bmc_classification['scores'][5]

        # # to debug, may delete later
        # top3_categories = bmc_classification['labels'][0:3]
        # log.debug(f'BMC elements: {top3_categories}')
        # top3_scores = bmc_classification['scores'][0:3]
        # log.debug(f'BMC scores: {top3_scores}')

        #return top3_category_ids

if __name__ == '__main__':
    # dummy sentence test
    sequence_to_classify = "Das Licht ist sehr angenehm und nicht zu kalt. Mich hat überrascht, dass das Licht doch sehr gut gestreut wird. Die alte, stromfressende Glühbirne vermisse ich also nicht!"
    obj = RobertaClassification()
    obj.mapping_reviews_bmc(sequence_to_classify, sequence_to_classify, threshold=0.85)
