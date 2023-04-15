class Solution:
    def __method1 (self, transactions):
        for i in range(len(transactions)):
            temp = transactions[i].split(',') ; temp[1], temp[2] = int(temp[1]), int(temp[2])
            transactions[i] = temp
        tran_is_valid_arr = [True for i in range(len(transactions))]
        transactions.sort(key=lambda x: x[1])
        for i in range(len(transactions)):
            j = i + 1
            while ((j < len(transactions)) and ((transactions[j][1] - transactions[i][1]) <= 60)):
                if ((transactions[i][0] == transactions[j][0]) and ((transactions[i][3] != transactions[j][3]))):
                    tran_is_valid_arr[i] = False
                    tran_is_valid_arr[j] = False
                j += 1
            if (transactions[i][2] > 1000): tran_is_valid_arr[i] = False
        return [",".join(map(str, transactions[i])) for i in range(len(transactions)) if (not tran_is_valid_arr[i])]

    def __method2 (self, transactions):
        hm, res = {}, []
        for i in range(len(transactions)):
            temp = transactions[i].split(',') ; temp[1], temp[2] = int(temp[1]), int(temp[2])
            if (temp[0] not in hm): hm[temp[0]] = []
            hm[temp[0]].append((temp[1], temp[2], temp[3]))
        for tr_nm in hm.keys():
            for tr_tm, tr_amt, tr_cty in hm[tr_nm]:
                if (tr_amt > 1000):
                    res.append("{},{},{},{}".format(tr_nm, tr_tm, tr_amt, tr_cty))
                    continue
                for nxt_tr_tm, nxt_tr_amt, nxt_tr_cty in hm[tr_nm]:
                    if ((abs(nxt_tr_tm - tr_tm) <= 60) and (nxt_tr_cty != tr_cty)):
                        res.append("{},{},{},{}".format(tr_nm, tr_tm, tr_amt, tr_cty))
                        break
        return res

    def invalidTransactions (self, transactions: List[str]) -> List[str]:
        return self.__method1(transactions)
        #return self.__method2(transactions)
