package de.dfki.sse.ri;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import de.dfki.sse.ri.core.RIReachabilityStrategy;
import de.dfki.sse.ri.model.Model;
import de.dfki.sse.ri.parser.SystemParser;
import de.dfki.sse.ri.parser.UserParser;

public class Main {


  public static void main(String args[]) throws IOException {
    String systemConfig = Files.readString(Paths.get("config/system/system_config_demo.json"));
    String userConfig = Files.readString(Paths.get("config/user/user_config_personal_gu.json"));
    Model model = new Model();
    SystemParser.parse(systemConfig, model);
    UserParser.parse(userConfig, model);
    RIReachabilityStrategy riStrategy = new RIReachabilityStrategy();
    float oldRI = riStrategy.calculateRI(model);
    riStrategy.transform(model);
    float newRI = riStrategy.calculateRI(model);
    System.out.println("Old RI: " + oldRI);
    System.out.println("New RI: " + newRI);
    System.out.println("Diff: " + Math.abs(newRI - oldRI));
  }

}
