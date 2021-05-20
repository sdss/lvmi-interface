# Basic idea is that KHU writes LVMi module.
import LVM_instrument as LVMi, LVM_survey as LVMs




def handle(fun, pars):

    log("Called %s with %s" % (fun,pars))




def main_loop():

    LVMs.connect()
    LVMi.connect()

    running = True
    safe = True

    while running:

        # examples of next_fun might be:
        # arclamps or flats
        # open dome
        # observe a field
        # I sort of think of next_fun as a script
        # A good example of next_fun is "handle_typical_observation"
        next_fun, next_pars = LVMs.get_next()

        if not safe:
            next_fun = emergency_shutdown_function
            next_pars = None

        try:
            LVMi.handle(next_fun, next_pars)
        except FieldExceptionError:
            # This category of error means there's an issue with the instructions
            # at this point in time. Examples are:
            # Airmass limit not respected, can't guide, whatever.
            # In short, the instructions provided are the issue
            log(something)
        except SafetyExceptionError:
            # This category of error means there's a safety issue that's not
            # related to the field, but not catastrophic. Weather, fog, etc.
            log(something)
        except InstrumentFailure:
            # The instrument software can't recover and external intervention
            # is needed
            log(something)
            safe = False
        




