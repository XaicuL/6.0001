# # # # #########################
# # # # ## EXAMPLE: returning a tuple
# # # # #########################
# # # # x = int(input("input a number: "))
# # # # y = int(input("input another number: "))
# # # #
# # # # def quotient_and_remainder(x, y):
# # # #     q = x // y
# # # #     r = x % y
# # # #     return (q, r)
# # # #
# # # #
# # # # (quot, rem) = quotient_and_remainder(x,y)
# # # # print('Your Q is ',quot)
# # # # print('Your R is' ,rem)
# # # #
# # # # # while quot == rem:
# # # # #     if rem != 0:
# # # # #         print('your r is not zero')
# # # # #     else:
# # # # #         print('your r is zero')
# # # # #         continue
# # #
# # #
# # # #
# # # #
# # # # #########################
# # # # ## EXAMPLE: iterating over tuples
# # # # #########################
# # # def get_data(aTuple):
# # #     """
# # #     aTuple, tuple of tuples (int, string)
# # #     Extracts all integers from aTuple and sets
# # #     them as elements in a new tuple.
# # #     Extracts all unique strings from from aTuple
# # #     and sets them as elements in a new tuple.
# # #     Returns a tuple of the minimum integer, the
# # #     maximum integer, and the number of unique strings
# # #     """
# # #     nums = ()  # empty tuple
# # #     words = ()
# # #     for t in aTuple:
# # #         # concatenating with a singleton tuple
# # #         nums = nums + (t[0],)
# # #         # only add words haven't added before
# # #         if t[1] not in words:
# # #             words = words + (t[1],)
# # #     min_n = min(nums)
# # #     max_n = max(nums)
# # #     unique_words = len(words)
# # #     return (min_n, max_n, unique_words)
# # #
# # #
# # # test = ((1, "a"), (2, "b"),
# # #         (1, "a"), (7, "b"))
# # # (a, b, c) = get_data(test)
# # # # print("a:", a, "b:", b, "c:", c)
# # #
# # # # ###
# # # # 리스트는 객체 자체를 수정(mutate)할 수 있지만,
# # # # 튜플은 불변이므로 객체는 절대 수정되지 않고
# # # # = 를 통해 변수가 가리키는 ‘대상’을 새 객체로 바꾼다.
# # # # 즉, 튜플 연산은 바인딩 변경(binding change)이다.
# # # # ###
# # # #
# # # # apply to any data you want!
# # # tswift = ((2014, "Katy"),
# # #           (2014, "Harry"),
# # #           (2012, "Jake"),
# # #           (2010, "Taylor"),
# # #           (2008, "Joe"))
# # # (min_year, max_year, num_people) = get_data(tswift)
# # # print("From", min_year, "to", max_year, \
# # #       "Taylor Swift wrote songs about", num_people, "people!")
# # # #
# # # #
# # # # #########################
# # # # ## EXAMPLE: sum of elements in a list
# # # # #########################
# #
# #
# #
# # def sum_elem_method1(L): #~Pythonic
# #     total = 0
# #     for i in range(len(L)):
# #         total += L[i]
# #     return total
# #
# #
# # def sum_elem_method2(L): #Pythonic
# #     total = 0
# #     for i in L:
# #         total += i
# #     return total
# #
# #
# # print(sum_elem_method1([1, 2, 3, 4]))
# # print(sum_elem_method2([1, 2, 3, 4]))
# #
# # #sum_elem_method1 is ~Pythonic, sum_elem_method2 is Pythonic
# #
# #
# # # #
# # # # #########################
# # # # ## EXAMPLE: various list operations
# # # # ## put print(L) at different locations to see how it gets mutated
# # # # #########################
# from traceback import print_tb
#
# # L1 = [2, 1, 3]
# # L2 = [4, 5, 6]
# # L3 = L1 + L2
# # L4 = (L1 + L2) * 2
# # L5 = L3 * 2
# # print(L5)
#
#
# # print(L4) #[2, 1, 3//L1 4, 5, 6//L2 2, 1, 3//L1 4, 5, 6//L2]
# # print(L2)
# # print(L3)
#
# # L1.extend([0, 6])
# # # print(L1)
# #
# # L = [2, 1, 3, 6, 3, 7, 0]
# # L.remove(2)
# # L.remove(3)
# # current L = [1,6,3,7,0]
# # # print(L)
# #
# # del (L[1]) #index position 1 = 1
# #
# # print(L) #[1, 3, 7, 0] del 6
# # x = L.pop()  <-- .pop은 '삭제(del)' 기능과 '값 반환(return)' 기능을 동시에 수행한다.
#
# # L100 = [0, 1, 2] 일 때:
#
# # 1. 인덱스 지정 X: L100.pop()
# #    = 마지막 요소(2)를 삭제(del)하고, 그 값 2를 반환(out 2)한다.
# #    L100은 [0, 1]이 됨.
# #    (메모: pop()의 기본 동작은 Stack의 'Pop'처럼 맨 끝을 건드린다.)
#
# # 2. 인덱스 지정 O: L100.pop(0)
# #    = 인덱스 0의 요소(0)를 삭제(del)하고, 그 값 0을 반환(out 0)한다.
# #    L100은 [1, 2]가 됨.
# #
# s = "I<3 cs"
# # print(list(s))
#
# # l = "Luciano"
# # print(list(l)) #['L', 'u', 'c', 'i', 'a', 'n', 'o']
#
# # print(s.split('<')) #['I', '3 cs']
#
# # L = ['a', 'b', 'c']
# # print(''.join(L)) #abc
# # print('_'.join(L)) #a_b_c
#
# # L = [9, 6, 0, 3]
# # #print(sorted(L)) #[0, 3, 6, 9] 오름차순 정리
# # x = reversed(L)
# # y = list(x)
# #
# # print(y)
#
# # L.sort()
#
# # ##########
# # L = [9, 6, 0, 3]
# #
# # # 1. reversed(L) 호출
# # x = reversed(L)
# # # -> x는 'list_reverseiterator' 객체(이터레이터)가 됨.
# # #    아직 리스트의 모든 요소를 역순으로 만든 것은 아님.
# #
# # # 2. list(x) 호출
# # y = list(x)
# # # -> 이터레이터 x가 가진 모든 요소를 순회하면서 새 리스트 y를 만듦.
# # #    이 시점에서 [3, 0, 6, 9]가 y에 저장됨.
# #
# # # 3. print(y) 출력
# # print(y)
# # # -> [3, 0, 6, 9] 출력!
#
# # # #
# # # # #########################
# # # # ## EXAMPLE: aliasing
# # # # #########################
# # a = 1
# # b = a
# # print(a)
# # print(b)
# #
# # # mutable , (list O/tuple X)
# #
# # warm = ['red', 'yellow', 'orange']
# # hot = warm
# # hot.append('pink')
# # print(hot)
# # print(warm)
#
# # # #
# # # # #########################
# # # # ## EXAMPLE: cloning
# # # # #########################
# # cool = ['blue', 'green', 'grey']
# # chill = cool[:] #copy every element
# # chill.append('black')
# # print(chill) #['blue', 'green', 'grey', 'black']
# # print(cool) #['blue', 'green', 'grey']
#
# #########################
# ## EXAMPLE: sorting with/without mutation
# # #########################
# # warm = ['red', 'yellow', 'orange']
# # sortedwarm = warm.sort()
# # print(warm) #['orange', 'red', 'yellow']
# # print(sortedwarm) #None
#
# # cool = ['grey', 'green', 'blue']
# # sortedcool = sorted(cool)
# # sortedhot = cool.sort()
# # print(cool) #['blue', 'green', 'grey']
# # print(sortedhot) #None
# # print(sortedcool) #['blue', 'green', 'grey']
# # #
# # # #########################
# # # ## EXAMPLE: lists of lists of lists...
# # # #########################
# # warm = ['yellow', 'orange']
# # hot = ['red']
# #
# # brightcolors = [warm]
# # brightcolors.append(hot)
# # print(brightcolors,'#1')
# #
# # hot.append('pink')
# # print(hot)
# # print(brightcolors,'#2, plus pink')
# # # #
# # # #
# # # # ###############################
# # # # ## EXAMPLE: mutating a list while iterating over it
# # # # ###############################
# # def remove_dups(L1, L2):
# #     for e in L1:
# #         if e in L2:
# #             L1.remove(e)
#
#
# # def remove_dups_new(L1, L2):
# #     L1_copy = L1[:] #L1_copy is all elements of L1
# #     for e in L1_copy:
# #         if e in L2:
# #             L1.remove(e)
# #
# #
# # L1 = [1, 2, 3, 4]
# # L2 = [1, 2, 5, 6]
# # # remove_dups(L1, L2)
# # print(L1, L2) #[2, 3, 4] [1, 2, 5, 6] // [2,3,4] : L1 , [1,2,5,6] : L2
# #
# # L1 = [1, 2, 3, 4]
# # L2 = [1, 2, 5, 6]
# # remove_dups_new(L1, L2)
# # print(L1, L2)
#
# # # # ###############################
# # # # ## EXERCISE: Test yourself by predicting what the output is and
# # # # ##           what gets mutated then check with the Python Tutor
# # # # ###############################
# cool = ['blue', 'green']
# warm = ['red', 'yellow', 'orange']
# print(cool)
# print(warm)
#
# colors1 = [cool]
# print(colors1)
# colors1.append(warm)
# print('colors1 = ', colors1)
#
# colors2 = [['blue', 'green'],
#            ['red', 'yellow', 'orange']]
# print('colors2 =', colors2)
#
# warm.remove('red')
# print('colors1 = ', colors1)
# print('colors2 =', colors2)
#
# for e in colors1:
#     print('e =', e)
#
# for e in colors1:
#     if type(e) == list:
#         for e1 in e:
#             print(e1)
#     else:
#         print(e)
#
# flat = cool + warm
# print('flat =', flat)
#
# print(flat.sort())
# print('flat =', flat)
#
# new_flat = sorted(flat, reverse=True)
# print('flat =', flat)
# print('new_flat =', new_flat)
#
# cool[1] = 'black'
# print(cool)
# print(colors1)

#function example

def max_val(x,y): #def function , name of function : max_val / list of formal parameters : x,y
    if x > y: #body of function start
        print('return x')
        return x
    else:
        print('return y')
        return y #body of funtion end


print(max_val(30,10))  #function call & assigned x,y
print(max_val(10,20))  #function call & assigned x,y