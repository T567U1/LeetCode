class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for domain in cpdomains:
            new_domain = domain.split(" ")
            split_domain = new_domain[-1].split('.')
            for i in range(len(split_domain)):
                #split domain and add it to dic if the domain is on dic just add times visited
                if '.'.join(split_domain[i:]) in dic:
                    dic['.'.join(split_domain[i:])] += int(new_domain[0])
                else:
                    dic['.'.join(split_domain[i:])] = int(new_domain[0])
                    
        return [str(dic[i]) + ' ' + i for i in dic.keys()]
