pin=3
print(wifi.sta.getip())
srv=net.createServer(net.TCP) 
srv:listen(1234,function(conn) 
    conn:on("receive",function (conn,payload)
      print(payload)
      if payload == '1'  then
          gpio.write(pin, gpio.HIGH)
      else
          gpio.write(pin, gpio.LOW)
      end
    print("send:",gpio.read(pin))
    conn:send(gpio.read(pin))
    end)
    conn:on("sent",function(conn) conn:close() end)
end)
