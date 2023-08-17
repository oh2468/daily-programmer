## https://old.reddit.com/r/dailyprogrammer/comments/5wnbsi/20170228_challenge_304_easy_little_accountant/

journals = """ACCOUNT;PERIOD;DEBIT;CREDIT;
1000;JAN-16;100000;0;
3000;JAN-16;0;100000;
7140;JAN-16;36000;0;
1000;JAN-16;0;36000;
1100;FEB-16;80000;0;
1000;FEB-16;0;60000;
2000;FEB-16;0;20000;
1110;FEB-16;17600;0;
2010;FEB-16;0;17600;
1000;MAR-16;28500;0;
4000;MAR-16;0;28500;
2010;MAR-16;17600;0;
1000;MAR-16;0;17600;
5000;APR-16;19100;0;
1000;APR-16;0;19100;
1000;APR-16;32900;0;
1020;APR-16;21200;0;
4000;APR-16;0;54100;
1000;MAY-16;15300;0;
1020;MAY-16;0;15300;
1000;MAY-16;4000;0;
4090;MAY-16;0;4000;
1110;JUN-16;5200;0;
2010;JUN-16;0;5200;
5100;JUN-16;19100;0;
1000;JUN-16;0;19100;
4120;JUN-16;5000;0;
1000;JUN-16;0;5000;
7160;JUL-16;2470;0;
2010;JUL-16;0;2470;
5500;JUL-16;3470;0;
1000;JUL-16;0;3470;"""

accounts = """ACCOUNT;LABEL;
1000;Cash;
1020;Account Receivables;
1100;Lab Equipement;
1110;Office Supplies;
2000;Notes Payables;
2010;Account Payables;
2110;Utilities Payables;
3000;Common Stock;
4000;Commercial Revenue;
4090;Unearned Revenue;
4120;Dividends;
5000;Direct Labor;
5100;Consultants;
5500;Misc Costs;
7140;Rent;
7160;Telephone;
9090;Dividends;"""

months = "JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split()

def process_query(query):
    acc_fr, acc_to, date_fr, date_to, form = query.split()
    blnc = [a.split(";") for a in journals.split("\n")[1::]]
    all_accs = [a.split(";") for a in accounts.split("\n")]

    debit = sum(int(a[2]) for a in blnc)
    credit = sum(int(a[3]) for a in blnc)
    if debit != credit:
        print("INVALID JOURNAL ACCOUNTING!")
        return None
    
    acc_fr = all_accs[1][0] if acc_fr == "*" else acc_fr.ljust(4, "0")
    acc_to = all_accs[-1][0] if acc_to == "*" else acc_to.ljust(4, "0")
    date_fr = blnc[0][1] if date_fr == "*" else date_fr
    date_to = blnc[-1][1] if date_to == "*" else date_to
    
    def date_lq(a, b):
        am, ad = a.split("-")
        bm, bd = b.split("-")
        ai, bi = months.index(am), months.index(bm)
        return ai <= bi or (ai == bi and int(ad) <= int(bd))

    blnc = [b for b in blnc if acc_fr <= b[0] <= acc_to]
    blnc = [b for b in blnc if date_lq(date_fr, b[1]) and date_lq(b[1], date_to)]
   
    counts = {}
    for b in blnc:
        key = b[0]
        if (c := counts.get(key, None)):
            d = int(b[2]) + c[0]
            c = int(b[3]) + c[1]
        else:
            d, c = int(b[2]), int(b[3])
        counts[key] = (d, c, d - c)
    
    accs_map = {a[0]: a[1] for a in all_accs}
    dates = sorted({b[1] for b in blnc}, key=lambda d: (months.index((x := d.split("-"))[0]), int(x[1])))
    counts = sorted(counts.items())
    pad = 16

    print(f"Total Debit :{debit} Total Credit :{credit}")
    print(f"Balance from account {acc_fr} to {acc_to} from period {dates[0]} to {dates[-1]}")
    print()
    print("Balance:")
    
    td = str(sum(v[0] for _, v in counts))
    tc = str(sum(v[1] for _, v in counts))
    tb = str(sum(v[2] for _, v in counts))
    
    if form == "TEXT":
        print("ACCOUNT         |DESCRIPTION     |           DEBIT|          CREDIT|         BALANCE|")
        print("-------------------------------------------------------------------------------------")
        for k, v in counts:
            print(f"{k.ljust(pad, ' ')}|{accs_map[k].ljust(pad, ' ')}|{str(v[0]).rjust(pad, ' ')}|{str(v[1]).rjust(pad, ' ')}|{str(v[2]).rjust(pad, ' ')}|")
        print(f"{'TOTAL'.ljust(pad, ' ')}|{''.ljust(pad, ' ')}|{td.rjust(pad, ' ')}|{tc.rjust(pad, ' ')}|{tb.rjust(pad, ' ')}|")
    else:
        print("ACCOUNT;DESCRIPTION;DEBIT;CREDIT;BALANCE;")
        for k, v in counts:
            print(f"{k};{accs_map[k]};{v[0]};{v[1]};{v[2]};")
        print(f"TOTAL;;{td};{tc};{tb};")
    

process_query("* 2 * FEB-16 TEXT")
print()
process_query("40 * MAR-16 * CSV")
