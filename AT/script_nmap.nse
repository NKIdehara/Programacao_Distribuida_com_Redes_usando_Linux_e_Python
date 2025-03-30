ortrule = function(host, port)
    return port.state == "open"
end

action = function(host, port)
    local output = string.format("servico em %s:%d...", host.ip, port.number)
    local service = port.service or "desconhecido"
    output = output .. "\nidentificado: " .. service
    return output
end
