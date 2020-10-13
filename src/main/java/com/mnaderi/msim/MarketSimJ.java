package com.mnaderi.msim;

import java.nio.file.Paths;

import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;
import org.apache.commons.lang3.time.StopWatch;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.mnaderi.msim.core.Utils;

public class MarketSimJ {

    private Logger log;

    private String configFileName;
    private int runNum = -1;
    private String runId;
    private long seed = 0;

    public static void main(String[] args) {
        // Sys.printClassPath();
        MarketSimJ instance = new MarketSimJ();
        instance.run(args);
    }

    public MarketSimJ() {
    }

    public void run(String[] args) {

        try {
            parse_args(args);
            init();
            run();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void parse_args(String[] args) throws Exception {
        Options options = new Options();

        Option optConfig = new Option("c", "config", true, "config file path");
        optConfig.setRequired(true);
        options.addOption(optConfig);

        Option optRun = new Option("r", "run", true, "run number");
        optRun.setRequired(true);
        optRun.setType(Integer.class);
        options.addOption(optRun);

        Option optLogDir = new Option("l", "log", true, "log directory");
        optLogDir.setRequired(false);
        options.addOption(optLogDir);

        CommandLineParser parser = new DefaultParser();
        HelpFormatter formatter = new HelpFormatter();
        CommandLine cmd;
        try {
            cmd = parser.parse(options, args);
        } catch (ParseException e) {
            System.out.println(e.getMessage());
            formatter.printHelp("MarketSim", options);

            throw new IllegalArgumentException("Error parsing command line");
        }

        configFileName = cmd.getOptionValue("config");
        String runArg = cmd.getOptionValue("run");
        System.setProperty("msim.experiment_run", runArg);
        runNum = Integer.parseInt(runArg);
        String logDir = cmd.getOptionValue("log", ".");
        System.setProperty("msim.log_dir", logDir);
        //-Dmsim.experiment_name=ch03_platform_performance_P100
        String experimentFile = Paths.get(configFileName).getFileName().toString();
        String experimentName = experimentFile.substring(0, experimentFile.length()-5);
        System.setProperty("msim.experiment_name", experimentName);
        
        log = LogManager.getLogger(MarketSimJ.class);
    }

    private void init() throws Exception {
    }

    private void run() throws Exception {
        StopWatch stopWatch = new StopWatch();
        stopWatch.start();
        stopWatch.stop();
        log.info("simulation completed successfully in {} ", Utils.formatStopWatch(stopWatch));
    }
}
