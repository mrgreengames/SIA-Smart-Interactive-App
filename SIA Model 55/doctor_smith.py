# Doctor Smith 3.0
import datetime

try:
    from SIA_APP import *
except ModuleNotFoundError:
    print("I can't find SIA!")
    print("SIA has to visit the surgery in order for me to do checkups on SIA!")


class DoctorSmith:
    def __init__(self):
        pass

    @staticmethod
    def test_protocol(protocol):
        print('Testing protocol %d' % protocol)
        try:
            protocol_check(protocol)
            print('Protocol %d is not working!')
            nw_prot.append('protocol %d' % protocol)
        except MissingFilesProtocol:
            print('Protocol %d is working!' % protocol)
            w_prot.append('protocol %d' % protocol)
        except EmergencyProtocol:
            print('Protocol %d is working!' % protocol)
            w_prot.append('protocol %d' % protocol)
        except IncorrectPasswordProtocol:
            print('Protocol %d is working!' % protocol)
            w_prot.append('protocol %d' % protocol)
        except MissingImportsProtocol:
            print('Protocol %d is working!' % protocol)
            w_prot.append('protocol %d' % protocol)
        except WrongPyInterpreterProtocol:
            print('Protocol %d is working!' % protocol)
            w_prot.append('protocol %d' % protocol)
        except ExtensionNotFoundProtocol:
            print('Protocol %d is working!' % protocol)
            w_prot.append('protocol %d' % protocol)
        except IncorrectEmailProtocol:
            print('Protocol %d is working!' % protocol)
            w_prot.append('protocol %d' % protocol)
        except ExtensionNotRealProtocol:
            print('Protocol %d is working!' % protocol)
            w_prot.append('protocol %d' % protocol)
        except UsedKeyProtocol:
            print('Protocol %d is working!' % protocol)
            w_prot.append('protocol %d' % protocol)

    @staticmethod
    def test_extern_obs(extern_obs):
        print('Testing %s' % extern_obs)
        test = doctor_smith_ask(extern_obs)
        if test == extern_obs:
            print('%s works!' % extern_obs)
            w_obs.append(extern_obs)
        else:
            print('%s doesn\'t works!' % extern_obs)
            nw_obs.append(extern_obs)


class FinalReport:
    def __init__(self):
        pass

    @staticmethod
    def create_report_file():
        global report_name
        now = datetime.datetime.now()
        report_name = 'diagnostic_report {} {} {} {}'.format(now.year, now.month, now.day, now.hour)

        f = open(report_name, 'x')
        f.close()


    @staticmethod
    def check_booleans(w_prot, nw_prot, w_obs, nw_obs):
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

        if len(w_obs) == 7:
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

        bool_dictionary = {'obs': all_w_obs, 'prot': all_w_prot}
        return bool_dictionary

    @staticmethod
    def write_report(all_w_prot, all_w_obs):
        global report_name

        report = open(report_name, 'w')
        if all_w_prot and all_w_obs:
            report.write('SIA is working fine! All protocols and extern-obs are working.')
            report.write('')
            report.write('The working protocols are {} and the working extern-obs are {} '.format(w_prot, w_obs))
            report.write('')
            report.write('Until the next checkup, bye!')
        elif all_w_prot and not all_w_obs:
            report.write("SIA has a nasty case of external flu. Not all of SIA's external objects are working.")
            report.write('')
            report.write('The working protocols are {} and the working extern-obs are {}'.format(w_prot, w_obs))
            report.write('')
            report.write('The not working external objects are {}'.format(nw_obs))
            report.write('')
            report.write('Please make a bug report at https://github.com/mrgreengames/SIA-Smart-Interactive-App/issues')
            report.write('')
            report.write("Come back after a few days. 'Til then, goodbye!")
        elif not all_w_prot and all_w_obs:
            report.write(
                "SIA has somehow caught a terrible case of the protocol flu. Not all the protocols are working!")
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

        report.close()


if __name__ == '__main__':
    w_prot = list()
    nw_prot = list()
    w_obs = list()
    nw_obs = list()
    all_w_prot = bool()
    all_w_obs = bool()
    doctor_smith = DoctorSmith
    for i in range(10):
        if i == 0 or i == 3:
            continue
        else:
            doctor_smith.test_protocol(i)

    doctor_smith.test_extern_obs('calc')
    doctor_smith.test_extern_obs('ngg')
    doctor_smith.test_extern_obs('search')
    doctor_smith.test_extern_obs('email')
    doctor_smith.test_extern_obs('app')
    doctor_smith.test_extern_obs('diction')
    doctor_smith.test_extern_obs('goback')
    doctor_smith.test_extern_obs('')

    final_report = FinalReport
    final_report.create_report_file()
    bool_dict = final_report.check_booleans(w_prot, nw_prot, w_obs, nw_obs)
    final_report.write_report(bool_dict['prot'], bool_dict['obs'])
