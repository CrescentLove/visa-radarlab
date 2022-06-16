import pyvisa

AWGtcpip = 'TCPIP0::localhost::inst2::INSTR'
Lecorytcpip = 'TCPIP0::169.254.254.64::inst0::INSTR'

if __name__ == '__main__':
    res = pyvisa.ResourceManager()
    print(res)  # 查看后端配置（IVI或pyvisa-py）
    print(res.list_resources())  # 查看已有设备
    my_instrument = res.open_resource(Lecorytcpip)  # 打开某一设备
    print('打开设备', my_instrument)
    print(my_instrument.query('*IDN?'))  # 发送查询指令
    print(res.list_opened_resources())  # 查看已通信设备

    my_instrument.write('*CLS')         # 清空所有事件寄存器
    print(my_instrument.query(':SYSTem:HELP:HEADers?'))