import time

from netmiko import ConnectHandler
import json

ORDERED_ALL_DEVICES = [
    {'device': 'ROUTER_RD',
     'config_archive': 'ROUTER_RD.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.1',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'ROUTER_1',
     'config_archive': 'ROUTER_1.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.6',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'ROUTER_2',
     'config_archive': 'ROUTER_2.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.145',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'ROUTER_3',
     'config_archive': 'ROUTER_3.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.13',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'SWITCH_1',
     'config_archive': 'SWITCH_1.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.146',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'SWITCH_2',
     'config_archive': 'SWITCH_2.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.147',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'SWITCH_3',
     'config_archive': 'SWITCH_3.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.148',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }}

]

AUTOMATED_CONFIGURATION_ORDER = [
    {'device': 'SWITCH_3',
     'config_archive': 'SWITCH_3.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.148',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'SWITCH_2',
     'config_archive': 'SWITCH_2.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.147',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'SWITCH_1',
     'config_archive': 'SWITCH_1.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.146',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'ROUTER_2',
     'config_archive': 'ROUTER_2.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.145',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'ROUTER_3',
     'config_archive': 'ROUTER_3.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.13',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'ROUTER_1',
     'config_archive': 'ROUTER_1.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.6',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'ROUTER_RD',
     'config_archive': 'ROUTER_RD.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.1',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }}
]

ORDERED_ROUTERS = [
    {'device': 'ROUTER_1',
     'config_archive': 'ROUTER_1.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.6',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'ROUTER_2',
     'config_archive': 'ROUTER_2.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.145',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'ROUTER_3',
     'config_archive': 'ROUTER_3.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.13',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'ROUTER_RD',
     'config_archive': 'ROUTER_RD.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.1',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }}
]

AUTOMATED_CONFIGURATION_ROUTERS = [
    {'device': 'ROUTER_2',
     'config_archive': 'ROUTER_2.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.145',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'ROUTER_3',
     'config_archive': 'ROUTER_3.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.13',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'ROUTER_1',
     'config_archive': 'ROUTER_1.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.6',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'ROUTER_RD',
     'config_archive': 'ROUTER_RD.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.1',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }}
]

ORDERED_SWITCHES = [
    {'device': 'SWITCH_1',
     'config_archive': 'SWITCH_1.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.146',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'SWITCH_2',
     'config_archive': 'SWITCH_2.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.147',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'SWITCH_3',
     'config_archive': 'SWITCH_3.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.148',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }}
]

AUTOMATED_CONFIGURATION_SWITCHES = [
    {'device': 'SWITCH_3',
     'config_archive': 'SWITCH_3.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.148',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'SWITCH_2',
     'config_archive': 'SWITCH_2.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.147',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
    {'device': 'SWITCH_1',
     'config_archive': 'SWITCH_1.txt',
     'device_data': {
         'device_type': 'cisco_ios',
         'host': '192.168.0.146',
         'username': 'eigrp_redes',
         'password': 'cafe_123@'
     }},
]


# Funcion que manda los comandos de configuracion desde un archivo de texto

class Router:
    @classmethod
    def sh_ip_route(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh ip route"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)

        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispoSitivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")

    @classmethod
    def sh_ip_protocol(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh ip protocol"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)
        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispoSitivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")

    @classmethod
    def sh_eigrp_n(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh ip eigrp neighbors"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)

        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispoSitivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")

    @classmethod
    def sh_eigrp_top(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh ip eigrp topology"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)

        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispoSitivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")

    @classmethod
    def dhcp_show(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh ip dhcp binding"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)

        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispoSitivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")

    @classmethod
    def sh_k_values(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh ip protocol | in metric", "do sh ip protocol | in Metric"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)
        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispositivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")


class Switch:
    @classmethod
    def sh_vlan_int(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh vlan"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)
        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispositivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")

    @classmethod
    def sh_int_trunk(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh interface trunk"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)
        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispositivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")

    @classmethod
    def sh_spanning_tree(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh spanning-tree"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)
        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispositivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")

    @classmethod
    def sh_ether_summ(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh etherchannel summary"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)
        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispositivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")

    @classmethod
    def sh_vtp_status(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh vtp status"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)
        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispositivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")


class GeneralDevice:
    @classmethod
    def conf_device(cls, device, config_archive):
        try:
            device_connection = ConnectHandler(**device)
            output_cli_device = device_connection.send_config_from_file(config_archive)
            print(output_cli_device)
        except Exception as err:
            print("\nLa conexion falló, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Tienes los privilegios necesarios\n"
                  "3.- La ip del host es correcta\n")

    # Funcion que imprime el comando sh running config

    @classmethod
    def shwrun_conf(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh run"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)
        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispositivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")

    @classmethod
    def cdp_neigh(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh cdp neighbors"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)

        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispoSitivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")

    # Funcion que imprime el comando do sh ip int brief
    @classmethod
    def sh_brief(cls, device):
        try:
            device_connection = ConnectHandler(**device)
            command = ["do sh ip int brief"]
            output_cli_device = device_connection.send_config_set(command)
            print(output_cli_device)
        except Exception as err:
            print("\nLa configuracion no pudo ser transmitida al dispositivo, asegurate de que:\n\n"
                  "1.- La conexion es correcta\n"
                  "2.- Estas conectado en la misma red\n"
                  "3.- La ip del host es correcta\n"
                  "4.- Tus dispositivos esten encendidos\n\n")


class Tools:
    @classmethod
    def find_device(cls, device_name):
        try:
            device_find = next(item for item in ORDERED_ALL_DEVICES if item["device"] == device_name)
            return device_find
        except Exception as err:
            return None


# Funcion que imprime el comando ip route

def main():
    print("========== Bienvenido a la interfaz de configuracion de dispositivos Cisco ==========\n"
          "========== ¿Que accion desea realizar? ==========\n"
          "1.-Realizar la configuracion inicial\n\n"
          "2.-Usar comando Show running config\n\n"
          "3.-Usar comando Show vlan\n\n"
          "4.-Usar comando Show Ip Route\n\n"
          "5.-Usar comando Show Ip int brief\n\n"
          "6.-Usar comando Show CDP Neighbors\n\n"
          "7.-Ip protocol\n\n"
          "8.-Ip EIGRP Neighbors\n\n"
          "9.-Ip EIGRP Topology\n\n"
          "10.-Show ip dhcp binding\n\n"
          "11.-Show interface trunk\n\n"
          "12.-Show spanning-tree\n\n"
          "13.-Show etherchannel summary\n\n"
          "14.-Show K Values\n"
          "-------------------------------------------------------------------------------------")

    menu_choose_function_value = int(input("Digite el numero:\n"))

    if menu_choose_function_value == 1:
        des = int(input("¿Desea configurar todos los dispositivos o alguno en especifico?"
                        "\n0.- Especifico"
                        "\n1.- Todos"
                        "\n2.-Todos los switches"
                        "\n3.-Todos los routers\n"))
        if des == 0:
            print("\n\nLista de dispositivos:\n\n")
            for device in ORDERED_ALL_DEVICES:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                config_archive = device_found.get('config_archive')
                print(device_found.get('device'))
                GeneralDevice.conf_device(cisco_881, config_archive)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        elif des == 2:
            for device in AUTOMATED_CONFIGURATION_SWITCHES:
                cisco_881 = device.get('device_data')
                config_archive = device.get('config_archive')
                print(device.get('device'))
                GeneralDevice.conf_device(cisco_881, config_archive)
        elif des == 3:
            for device in AUTOMATED_CONFIGURATION_ROUTERS:
                cisco_881 = device.get('device_data')
                config_archive = device.get('config_archive')
                print(device.get('device'))
                GeneralDevice.conf_device(cisco_881, config_archive)
        else:
            for device in AUTOMATED_CONFIGURATION_ORDER:
                cisco_881 = device.get('device_data')
                config_archive = device.get('config_archive')
                print(device.get('device'))
                GeneralDevice.conf_device(cisco_881, config_archive)
    elif menu_choose_function_value == 2:
        decision_value = int(input("¿De que dispositivo desea obtener la running-configuration?"
                                   "\n0.- Especifico"
                                   "\n1.- Todos"
                                   "\n2.-Todos los switches"
                                   "\n3.-Todos los routers\n"))
        if decision_value == 0:
            print("\n\nLista de dispositivos:\n\n")
            for device in ORDERED_ALL_DEVICES:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                GeneralDevice.shwrun_conf(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        elif decision_value == 2:
            for device in ORDERED_SWITCHES:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                GeneralDevice.shwrun_conf(cisco_881)
        elif decision_value == 3:
            for device in ORDERED_ROUTERS:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                GeneralDevice.shwrun_conf(cisco_881)
        else:
            for device in ORDERED_ALL_DEVICES:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                GeneralDevice.shwrun_conf(cisco_881)
    elif menu_choose_function_value == 3:
        decision_value = int(input("¿En que switch desea ver las interfaces vlan configuradas?"
                                   "\n0.- Especifico"
                                   "\n1.- Todos\n"))
        if decision_value == 0:
            print("\n\nLista de switches:\n\n")
            for device in ORDERED_SWITCHES:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                Switch.sh_vlan_int(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        else:
            for device in ORDERED_SWITCHES:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                Switch.sh_vlan_int(cisco_881)
        print("\n ----- Ctr+c para salir ----- \n")
    elif menu_choose_function_value == 4:
        decision_value = int(input("¿De cual router desea obtener su tabla de routeo?"
                                   "\n0.- Especifico"
                                   "\n1.- Todos\n"))
        if decision_value == 0:
            print("\n\nLista de routers:\n\n")
            for device in ORDERED_ROUTERS:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                Router.sh_ip_route(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        else:
            for device in ORDERED_ROUTERS:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                Router.sh_ip_route(cisco_881)
    elif menu_choose_function_value == 5:
        decision_value = int(input("¿Desea obtener el sh ip interface brief de un dispositivo en especifico o de todos?"
                                   "\n0.- Especifico"
                                   "\n1.- Todos\n"))
        if decision_value == 0:
            print("\n\nLista de dispositivos:\n\n")
            for device in ORDERED_ALL_DEVICES:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                GeneralDevice.sh_brief(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        else:
            for device in ORDERED_ALL_DEVICES:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                GeneralDevice.sh_brief(cisco_881)
        print("\n ----- Ctr+c para salir ----- \n")

    elif menu_choose_function_value == 6:
        decision_value = int(input("¿Obtener el cdp neighbors?"
                                   "\n0.- Especifico"
                                   "\n1.- Todos\n"))
        if decision_value == 0:
            print("\n\nLista de dispositivos:\n\n")
            for device in ORDERED_ALL_DEVICES:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                GeneralDevice.cdp_neigh(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        else:
            for device in ORDERED_ALL_DEVICES:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                GeneralDevice.cdp_neigh(cisco_881)
        print("\n ----- Ctr+c para salir ----- \n")
    elif menu_choose_function_value == 7:
        decision_value = int(input("¿Obtener el Ip protocol?"
                                   "\n0.- Especifico"
                                   "\n1.- Todos\n"))
        if decision_value == 0:
            print("\n\nLista de routers:\n\n")
            for device in ORDERED_ROUTERS:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                Router.sh_ip_protocol(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        else:
            for device in ORDERED_ROUTERS:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                Router.sh_ip_protocol(cisco_881)
    elif menu_choose_function_value == 8:
        decision_value = int(input("Comando para obtener EIGRP Neighbors"
                                   "\n0.- Especifico"
                                   "\n1.- Todos\n"))
        if decision_value == 0:
            print("\n\nLista de routers:\n\n")
            for device in ORDERED_ROUTERS:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                Router.sh_eigrp_n(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        else:
            for device in ORDERED_ROUTERS:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                Router.sh_eigrp_n(cisco_881)
    elif menu_choose_function_value == 9:
        decision_value = int(input("Mostrar el comando EIGRP Topology"
                                   "\n0.- Especifico"
                                   "\n1.- Todos\n"))
        if decision_value == 0:
            print("\n\nLista de routers:\n\n")
            for device in ORDERED_ROUTERS:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                Router.sh_eigrp_top(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        else:
            for device in ORDERED_ROUTERS:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                Router.sh_eigrp_top(cisco_881)
    elif menu_choose_function_value == 10:
        decision_value = int(input("Obtener el comando dhcp binding"
                                   "\n0.- Especifico"
                                   "\n1.- Todos\n"))
        if decision_value == 0:
            print("\n\nLista de routers:\n\n")
            for device in ORDERED_ROUTERS:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                Router.dhcp_show(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        else:
            for device in ORDERED_ROUTERS:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                Router.dhcp_show(cisco_881)
    elif menu_choose_function_value == 11:
        decision_value = int(input("¿Desea Obtener las interfaces troncales?"
                                   "\n0.- Especifico"
                                   "\n1.- Todos\n"))
        if decision_value == 0:
            print("\n\nLista de switches:\n\n")
            for device in ORDERED_SWITCHES:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                Switch.sh_int_trunk(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        else:
            for device in ORDERED_SWITCHES:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                Switch.sh_int_trunk(cisco_881)
    elif menu_choose_function_value == 12:
        decision_value = int(input("Obtener comando sh spanning tree"
                                   "\n0.- Especifico"
                                   "\n1.- Todos\n"))
        if decision_value == '0':
            print("\n\nLista de switches:\n\n")
            for device in ORDERED_SWITCHES:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                Switch.sh_spanning_tree(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        else:
            for device in ORDERED_SWITCHES:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                Switch.sh_spanning_tree(cisco_881)
    elif menu_choose_function_value == 13:
        decision_value = int(input("Obtener el comando de ether summary"
                                   "\n0.- Especifico"
                                   "\n1.- Todos\n"))
        if decision_value == 0:
            print("\n\nLista de switches:\n\n")
            for device in ORDERED_SWITCHES:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                Switch.sh_ether_summ(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        else:
            for device in ORDERED_SWITCHES:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                Switch.sh_ether_summ(cisco_881)
    elif menu_choose_function_value == 14:
        decision_value = int(input("Obtener el comando de k values"
                                   "\n0.- Especifico"
                                   "\n1.- Todos\n"))
        if decision_value == 0:
            print("\n\nLista de routers:\n\n")
            for device in ORDERED_ROUTERS:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                Router.sh_k_values(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        else:
            for device in ORDERED_ROUTERS:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                Router.sh_k_values(cisco_881)
    elif menu_choose_function_value == 15:
        decision_value = int(input("Obtener el status de VTP values"
                                   "\n0.- Especifico"
                                   "\n1.- Todos\n"))
        if decision_value == 0:
            print("\n\nLista de switches:\n\n")
            for device in ORDERED_SWITCHES:
                print(device.get('device'))
            device_search = input("\n\nIntroduzca el nombre del dispositivo tal cual aparece en la lista\n\n")
            device_found = Tools.find_device(device_search)
            if device_found:
                cisco_881 = device_found.get('device_data')
                print(device_found.get('device'))
                Switch.sh_vtp_status(cisco_881)
            else:
                print("\nEl dispositivo no esta en la lista\n")
        else:
            for device in ORDERED_SWITCHES:
                cisco_881 = device.get('device_data')
                print(device.get('device'))
                Switch.sh_vtp_status(cisco_881)
    else:
        print("Saliendo del programa...")
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("Gracias por usar!")
        exit()
    main()


if __name__ == '__main__':
    main()
