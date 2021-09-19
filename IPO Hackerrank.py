from collections import OrderedDict
def getUnallotetedUsers(bids, totalShares):
    bids = sorted(bids, key=lambda x:(-x[2], x[3]))
    price_groups = OrderedDict()
    un_users = []
    for r in bids:
        if r[2] not in price_groups:
            price_groups[r[2]] = [[r[0], r[1]]]
            un_users.append(r[0])
        else:
            price_groups[r[2]].append([r[0], r[1]])
            un_users.append(r[0])

    print(price_groups)
    
    for k, v in price_groups.items():
        print('Total Shares Now: ', totalShares)
        print("Current user id: ", v[0][0])
        if totalShares <= 0:
            break
        if len(v) == 1:
            print('Removing: ', v[0][0])
            un_users.remove(v[0][0])
            totalShares -= v[0][1]
        else:
            if totalShares < len(v):
                print('Removing: ', v[0][0])
                to_remove = v[: len(v) - totalShares][0]
                print('To remove: ', to_remove)
                price_groups[k] = v[(len(v) - totalShares + 1) :]
                for u in to_remove:
                    print('Trying to remove: ', u)
                    print('Un users: ', un_users)
                    if u in un_users:
                        print('Removing: ', u)
                        un_users.remove(u)
                break
            else:
                print('Current k,v: ', k, price_groups[k])
                for u in v:
                    un_users.remove(u[0])
                shares = sum(x[1] for x in v)
                totalShares -= shares
    
    return sorted(un_users)



def main():
    # bids = [[1,5,5,0], [2,7,8,1],[3,7,5,1], [4,10,3,3]]
    bids = [[1,2,5,0], [2,1,4,2], [3,5,4,6]]
    # totalShares = 18
    totalShares = 3
    print(getUnallotetedUsers(bids, totalShares))

if __name__== "__main__":
    main()