import re
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            ip = IP.split('.')
            if len(ip) != 4:
                return 'Neither'
            for bites in ip:
                if not bites or (len(bites) > 1 and bites[0] == '0') or bool(re.findall('[a-zA-Z-]', bites)) or int(bites) > 255 or len(bites) > 4:
                    return 'Neither'

            return 'IPv4'

        elif ':' in IP:
            ip = IP.split(':')
            if len(ip) != 8:
                return 'Neither'
            for bites in ip:
                if bites == '' or bool(re.findall(r'[^\w\s]', bites)) or bool(re.findall('[g-zG-Z]', bites)) or len(bites) > 4:
                    return 'Neither'

            return 'IPv6'
        else:
            return 'Neither'
