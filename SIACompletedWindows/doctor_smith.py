# Doctor Smith
# Ready to diagnose SIA!
w_prot = list()
nw_prot = list()
w_obs = list()
nw_obs = list()
import datetime

# Looking for SIA
try:
    from SIA_APP import *
except ModuleNotFoundError:
    print("I can't find SIA!")
    print("SIA has to visit the surgery in order for me to do checkups on SIA!")


# Test protocols
def test_protocols():
    print("Testing SIA's protocols")
    # Testing Protocol 1
    p('Testing protocol 1')
    try:
        protocol_check(1)
        print('Protocol 1 is not working!')
        nw_prot.append('protocol 1')
    except MissingFilesProtocol:
        p('Protocol 1 works!')
        w_prot.append('protocol 1')
    
    # Testing protocol 2
    p('Testing protocol 2')
    try:
        protocol_check(2, reason='checking if protocol 2 works!')
        print('Protocol 2 is not working!')
        nw_prot.append('protocol 2')
    except EmergencyProtocol:
        print('Protocol 2 is working!')
        w_prot.append('protocol 2')

    # Testing protocol 4
    p('Testing protocol 4')
    try:
        protocol_check(4)
        print('Protocol 4 is not working!')
        nw_prot.append('protocol 4')
    except MissingImportsProtocol:
        p('Protocol 4 works!')
        w_prot.append('protocol 4')

    # Testing protocol 5
    p('Testing protocol 5')
    try:
        protocol_check(5)
        print('Protocol 5 is not working!')
        nw_prot.append('protocol 5')
    except WrongPyInterpreterProtocol:
        p('Protocol 5 works!')
        w_prot.append('protocol 5')

    # Testing protocol 6
    p('Testing protocol 6')
    try:
        protocol_check(6)
        print('Protocol 6 is not working!')
        nw_prot.append('protocol 6')
    except ExtensionNotFoundProtocol:
        p('Protocol 6 works!')
        w_prot.append('protocol 6')

    # Testing protocol 7
    p('Testing protocol 7')
    try:
        protocol_check(7)
        print('Protocol 7 is not working!')
        nw_prot.append('protocol 7')
    except IncorrectEmailProtocol:
        p('Protocol 7 works!')
        w_prot.append('protocol 7')

    # Testing protocol 8
    p('Testing protocol 8')
    try:
        protocol_check(8)
        print('Protocol 8 is not working!')
        nw_prot.append('protocol 8')
    except ExtensionNotRealProtocol:
        p('Protocol 8 works!')
        w_prot.append('protocol 8')

    # Testing protocol 9
    try:
        protocol_check(9)
        print('Protocol 9 is not working!')
        nw_prot.append('protocol 9')
    except UsedKeyProtocol:
        print('Protocol 9 works!')
        w_prot.append('protocol 9')


# Test external objects
def test_extern_obs():
    # Testing calculator
    print("Testing calculator")
    test = doctor_smith_ask('calc', 'Doctor Smith', 'NaN', 'functions', 'sfn', 'data', 'password123',
                     'someone@example.com', 'DoctorSmithExtension')
    if test == 'chose calculator':
        print('Calculator works!')
        w_obs.append('calculator')
    else:
        print("Calculator doesn't work!")
        nw_obs.append('calculator')

    # Testing number guessing game
    print("Testing number guessing game")
    test = doctor_smith_ask('ngg', 'Doctor Smith', 'NaN', 'functions', 'sfn', 'data', 'password123',
                     'someone@example.com', 'DoctorSmithExtension')
    if test == 'chose number guessing game':
        print('Number guessing game works!')
        w_obs.append('number guessing game')
    else:
        print("Number guessing game doesn't work!")
        nw_obs.append('number guessing game')

    # Testing search engines
    print("Testing search engines")
    test = doctor_smith_ask('search', 'Doctor Smith', 'NaN', 'functions', 'sfn', 'data', 'password123',
                     'someone@example.com', 'DoctorSmithExtension')
    if test == 'chose the search object':
        print('search engines works!')
        w_obs.append('search engines')
    else:
        print("search engines doesn't work!")
        nw_obs.append('search engines')

    # Testing email sender
    print("Testing email sender")
    test = doctor_smith_ask('email', 'Doctor Smith', 'NaN', 'functions', 'sfn', 'data', 'password123',
                     'someone@example.com', 'DoctorSmithExtension')
    if test == 'chose the email object':
        print('email sender works!')
        w_obs.append('email sender')
    else:
        print("email sender doesn't work!")
        nw_obs.append('email sender')

    # Testing app launcher
    print("Testing app launcher")
    test = doctor_smith_ask('app', 'Doctor Smith', 'NaN', 'functions', 'sfn', 'data', 'password123',
                     'someone@example.com', 'DoctorSmithExtension')
    if test == 'chose app launcher':
        print('App launcher works!')
        w_obs.append('app launcher')
    else:
        print("App launcher doesn't work!")
        nw_obs.append('app launcher')

    # Testing dictionary
    print("Testing dictionary")
    test = doctor_smith_ask('diction', 'Doctor Smith', 'NaN', 'functions', 'sfn', 'data', 'password123',
                     'someone@example.com', 'DoctorSmithExtension')
    if test == 'chose the dictionary':
        print('Dictionary works!')
        w_obs.append('dictionary')
    else:
        print("Dictionary doesn't work!")
        nw_obs.append('dictionary')

    # Testing leaving the extern-obs selector
    print("Testing leaving the extern-obs selector")
    test = doctor_smith_ask('goback', 'Doctor Smith', 'NaN', 'functions', 'sfn', 'data', 'password123',
                     'someone@example.com', 'DoctorSmithExtension')
    if test == 'wants to go back':
        print('Leaving works!')
        w_obs.append('leaving the extern-obs selector')
    else:
        print("Leaving doesn't work!")
        nw_obs.append('leaving the extern-obs selector')

    # Testing inputing an extern-obs that doesn't exist
    print("Testing inputing an extern-obs that doesn't exist")
    test = doctor_smith_ask('$', 'Doctor Smith', 'NaN', 'functions', 'sfn', 'data', 'password123',
                     'someone@example.com', 'DoctorSmithExtension')
    if test == 'does not have that':
        print('inputing an extern-obs that doesn\'t exist works!')
        w_obs.append('inputing an extern-obs that doesn\'t exist')
    else:
        print("inputing an extern-obs that doesn't exist doesn't work!")
        nw_obs.append('inputing an extern-obs that doesn\'t exist')


# Determine the final diagnostic report
def determine_final_report(is_all_working_protocols, is_all_working_extern_obs):
    now = datetime.datetime.now()
    report_name = 'diagnostic_report {} {} {} {}'.format(now.year, now.month, now.day, now.hour)
        
    report = open(report_name, 'w')
    if is_all_working_protocols and is_all_working_extern_obs:
        report.write('SIA is working fine! All protocols and extern-obs are working.')
        report.write('')
        report.write('The working protocols are {} and the working extern-obs are {} '.format(w_prot, w_obs))
        report.write('')
        report.write('Until the next checkup, bye!')
    elif is_all_working_protocols and not is_all_working_extern_obs:
        report.write("SIA has a nasty case of external flu. Not all of SIA's external objects are working.")
        report.write('')
        report.write('The working protocols are {} and the working extern-obs are {}'.format(w_prot, w_obs))
        report.write('')
        report.write('The not working external objects are {}'.format(nw_obs))
        report.write('')
        report.write('Please make a bug report at https://github.com/mrgreengames/SIA-Smart-Interactive-App/issues')
        report.write('')
        report.write("Come back after a few days. 'Til then, goodbye!")
    elif not is_all_working_protocols and is_all_working_extern_obs:
        report.write("SIA has somehow caught a terrible case of the protocol flu. Not all the protocols are working!")
        report.write('')
        report.write('SIA needs to go straight to the hospital to have an emergency surgery! I will call the hospital and you fill out this form, https://github.com/mrgreengames/SIA-Smart-Interactive-App/issues/new?assignees=GreenGames%2C+SergeantLime&labels=security+vulnerability&template=doctor-smith-form.md&title=')
        report.write('')
        report.write('Working protocols are {} and working external objects are {}'.format(w_prot, w_obs))
        report.write('')
        report.write('Not working protocols are {}'.format(w_prot, w_obs))
        report.write('')
        report.write('Good luck!')
    else:
        report.write('SIA has a fatal illness! SIA needs to go straight to the hospital! Fill out this form https://github.com/mrgreengames/SIA-Smart-Interactive-App/issues/new?assignees=GreenGames%2C+SergeantLime&labels=bug%2C+help+wanted%2C+security+vulnerability&template=urgent.md&title=')
        report.write('')
        report.write('Not working protocols are {} and not working external objects are {}'.format(nw_prot, nw_obs))
        report.write('')
        report.write('Good luck!')
    

if __name__ == '__main__':
    all_w_prot = bool()
    all_w_obs = bool()
    test_protocols()
    test_extern_obs()
    if len(w_prot) > 0 and len(nw_prot) == 0:
        print('All protocols are working!')
        print('Working protocols are', w_prot)
        all_w_prot = True
    else:
        print('Not all protocols are working!')
        print('Please read this: https://github.com/mrgreengames/SIA-Smart-Interactive-App/security/policy')
        print('Working protocols are', w_prot)
        print('Not working protocols are', nw_prot)
        all_w_prot = False

    if len(nw_prot) == 8:
        print('There are no working protocols!')
        print('Please read this: https://github.com/mrgreengames/SIA-Smart-Interactive-App/security/policy')
        print('Now working protocols are', nw_prot)
        all_w_prot = False

    if len(w_obs) > 0 and len(nw_obs) == 0:
        print('All external objects are working!')
        print('Working external objects are', w_obs)
        all_w_obs = True
    else:
        print('Not all external objects are working!')
        print('Please open a bug report at https://github.com/mrgreengames/SIA-Smart-Interactive-App/issues')
        print('Working external objects are', w_obs)
        print('Not working external objects are', nw_obs)
        all_w_obs = False

    if len(w_obs) == 0:
        print('There are no working external objects!')
        print('Please open a bug report at https://github.com/mrgreengames/SIA-Smart-Interactive-App/issues')
        print('Not working external objects are', nw_obs)
        all_w_obs = False

    determine_final_report(all_w_prot, all_w_obs)
