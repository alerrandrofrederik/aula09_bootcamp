import sentry_sdk

sentry_sdk.init(
    dsn="https://b032121cd887d3c4b60fef388fe3d44c@o4508265567551488.ingest.us.sentry.io/4508265570369536",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
)

# Manually call start_profiler and stop_profiler
# to profile the code in between
sentry_sdk.profiler.start_profiler()
# this code will be profiled
#
# Calls to stop_profiler are optional - if you don't stop the profiler, it will keep profiling
# your application until the process exits or stop_profiler is called.
sentry_sdk.profiler.stop_profiler()

division_by_zero = 1 / 0