from konlpy.tag import Okt
import math

okt = Okt()
total_num = 0
total_pos = 0
total_neg = 0

def open_file(filename, flag):

    global total_num, total_pos, total_neg

    data = []
    
    with open(filename, 'r', encoding='UTF8') as f:
        if flag == 1:
            for line in f.read().splitlines():
                item = line.split('\t')
                if item[2] == '0':
                    total_neg = total_neg + 1
                    total_num = total_num + 1
                elif item[2] == '1':
                    total_pos = total_pos + 1
                    total_num = total_num + 1              
                data.append(item)
            total_num = math.log2(total_num)
            total_pos = math.log2(total_pos)
            total_neg = math.log2(total_neg)
        elif flag == 0:
            for line in f.read().splitlines():
                item = line.split('\t')
                data.append(item)

    data = data[1:]
        
    return data

def tokenize(doc):
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

def train(train_docs):

    train_result = {}
    
    for i in train_docs:

        temp = {}
        for j in i[0]:
            word = j.split('/')
            temp[word[0]] = True
        for j in temp.keys():
            if j not in train_result:
                train_result[j] = {'pos' : 0, 'neg' : 0}
            if i[1] == '1':
                train_result[j]['pos'] = train_result[j]['pos'] + 1
            elif i[1] == '0':
                train_result[j]['neg'] = train_result[j]['neg'] + 1

    for i in train_result.keys():
        if train_result[i]['pos'] != 0:
            train_result[i]['pos'] = math.log2(train_result[i]['pos'])
        if train_result[i]['neg'] != 0:
            train_result[i]['neg'] = math.log2(train_result[i]['neg'])

    return train_result

def naive_bayes(test_data, train_result):

    global total_num, total_pos, total_neg

    test_result = []
    
    for i in test_data:
        pos = total_pos - total_num
        neg = total_neg - total_num
    
        review = tokenize(i[1])

        for j in review:
            word = j.split('/')

            for k in word:
                if k in train_result:
                    pos = pos + (train_result[k]['pos'] - total_pos)
                    neg = neg + (train_result[k]['neg'] - total_neg)
        if pos >= neg:
            test_result.append(i[0] + '\t' + i[1] + '\t' + str(1) + '\n')
        else:
            test_result.append(i[0] + '\t' + i[1] + '\t' + str(0) + '\n')

    return test_result

def write_file(filename, test_result):
    
    with open(filename, 'w', encoding='UTF8') as f:
        for i in test_result:
            f.write(i)

def main():

    train_data = open_file('ratings_train.txt', 1)
    train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
    train_result = train(train_docs)
    
    test_data = open_file('ratings_test.txt', 0)
    test_result = naive_bayes(test_data, train_result)
    write_file('ratings_result.txt', test_result)
'''
    test_data = open_file('ratings_valid.txt', 0)
    test_result = naive_bayes(test_data, train_result)

    num = 0
    good = 0
    for i in range(len(test_result)):
        num = num + 1
        item = test_result[i].split('\t')
        if int(item[2]) == int(test_data[i][2]):
            good = good + 1

    print(good/num*100) #83.88
'''
if __name__ == "__main__":
    main()
