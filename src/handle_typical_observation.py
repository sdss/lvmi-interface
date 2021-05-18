

import LVM_instrument as LVMi

def logger(x):
    """ There will be a sophisticated facility logger, this is temporary"""
    print(x)

def handle_typical_observation(sci_field, sky1_field, sky2_field, spec_fields):
    """Example code for handling a typical observation

    Args:
        sci_field(4): (field name, ra, dec, exptime)
        sky1_field(4): as above but for the first sky field
        sky2_field(4): as above but for the second sky field
        sp_fields(N,4): Nx4tuple where N is the number of spectrophotometric stars


    """

    LVMi.sci_tel.goto(sci_field)
    LVMi.sky1_tel.goto(sky1_field)
    LVMi.sky2_tel.goto(sky2_field)
    LVMi.sky2_tel.goto(sp_fields[0])


    # Wait can throw exceptions; these will be captured in the calling 
    # function. 
    # Wait is blocking.
    # raises are there to bring attention to the higher-level actor
    # who will make all the hard decisions.
    try:
        LVMi.wait()
    except FieldNotAcquired(tel):
        # Telescope doesn't confirm perfect acquisition but guiding is OK
        # Start the exposures
        print("Telescope %s didn't acquire field" % tel)
    except GuidingFailure(tel):
        if tel is LVMI.sci_tel:
            # If the science telescope isn't guiding maybe then we want
            # to move to the next field.
            raise 
    except AirmassLimitError(tel):
        if tel is LVM.sci_tel:
            # Likely move to the next target
            raise
        if tel is LVM.sp_tel:
            raise
    except HardwareError:
        # Something bad happened
        raise 

    LVMi.spectrograph.expose(sci_field.exptime)

    wait(sp_fields[0].exptime)
    for sp_field in sp_fields[1:]:
        try:
            LVMi.sp_tel.goto_while_exposing(sp_field)
            # Note goto_while_exposing is likely a convenience wrapper around goto. Goto_while_exposing will add information to the headers
        except ... bunch of stuff:
            do something
        wait(sp_field.exptime)





    




    
