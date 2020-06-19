def verify(input)
  format= /\d\|\d{1}[x]\w{8}\|\d{1}[x]\w{8}$/
  if input.match(format)
    first=input.scan(/\d\|\d{1}[x]\w{8}\|\d{1}[x](\w{8})$/)
    first=first.flatten[0]
    num=input.scan(/\d\|\d{1}[x](\w{8})\|\d{1}[x]\w{8}$/)
    num=num.flatten[0]
    num1=num.scan(/(..)(..)(..)(..)/).map(&:reverse).join
    if first==num1
      return true
    else
      return false
    end
  else
    return false
  end
end
