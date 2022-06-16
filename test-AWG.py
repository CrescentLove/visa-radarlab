import pyvisa

AWGtcpip = 'TCPIP0::localhost::inst2::INSTR'
Lecorytcpip = 'TCPIP0::169.254.254.64::inst0::INSTR'

if __name__ == '__main__':
    res = pyvisa.ResourceManager()
    print(res)  # 查看后端配置（IVI或pyvisa-py）
    print(res.list_resources())  # 查看已有设备
    my_instrument = res.open_resource(AWGtcpip, resource_pyclass=pyvisa.resources.MessageBasedResource)  # 打开某一设备
    print('打开设备', my_instrument)
    print(my_instrument.query('*IDN?'))  # 发送查询指令
    print(res.list_opened_resources())  # 查看已通信设备

    my_instrument.write('*CLS')         # 清空所有事件寄存器

    # txt = my_instrument.query(':SYSTem:HELP:HEADers?')      # 读取所有该设备支持的SCPIcommand
    # with open('SCPIcommands.txt', 'w') as f:
    #     f.write(txt)

    # print(my_instrument.write('*RST'))  # RST指令不支持query

    # txt_SYSTSET = (my_instrument.query(':SYST:SET?'))    # 查询系统设置,或者使用*LRN？
    # with open('info_SYSTSET.txt', 'w') as f:
    #     f.write(txt_SYSTSET)


    ##############################################################
    # AWG预设，sample frequency & OutputEnable
    my_instrument.write(':FREQ:RAST 12000000000')  # 设定采样频率12G
    my_instrument.write(':OUTP1 ON;:OUTP2 ON')               # 打开两渠道


    ##############################################################
    # AWG操作
    # my_instrument.write(':INIT:IMM1')     # 打开channel1
    try:
        my_instrument.write(':ABOR1')  # 关闭channel1
        print('是否执行', my_instrument.query('*OPC?'))  # 确认上条指令执行
    except pyvisa.errors.VisaIOError as e:
        err = my_instrument.query(':SYST:ERR?')        # 读取错误队列第一条（FIFO）
        print(err)




