package com.mnaderi.msim.core;

import java.time.Duration;

import org.apache.commons.lang3.time.DurationFormatUtils;
import org.apache.commons.lang3.time.StopWatch;

public class Utils {

    public static String formatDuration(Duration duration) {
        return String.format("%d:%02d:%02d", duration.toHours(), duration.toMinutesPart(), duration.toSecondsPart());
    }

    public static String formatStopWatch(StopWatch stopWatch) {
        return DurationFormatUtils.formatDurationHMS(stopWatch.getTime());
    }
}
