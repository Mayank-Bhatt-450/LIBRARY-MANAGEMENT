print('''
ll       iiiiiiiiiii bbbbbb   rrrrrrr          aaaa        rrrrrrrr  yy      yy
ll       iiiiiiiiiii bb   bb  rr    rr        aaaaaa       rr     rr  yy    yy
ll            ii     bb    b  rr     r       aa    aa      rr      r   yy  yy
ll            ii     bbbbbb   rrrrrrr       aaaaaaaaaa     rrrrrrrr     yyyy
ll            ii     bb   bb  rr   rr      aaaaaaaaaaaa    rr    rr      yy
llllllll iiiiiiiiiii bb    b  rr    rr    aa          aa   rr     rr     yy
llllllll iiiiiiiiiii bbbbbb   rr     rr  aa            aa  rr      rr    yy

                                    MANAGEMENT''')
p=2
p2="physics"
c=2
c2="chemistry"
m=2
m2="maths"
ans='y'
while True:
    if ans=='y':    
        print('1) issue a book.')
        print('2) return book')
        print('3) replace book ')
        print('4) status of books available ')
        a=int(input('ener your option :'))
        if a==1:
            print('1)'+str(p2))
            print('2)'+str(c2))
            print('3)'+str(m2))
            b=int(input('ener your choice :'))
            if b==1:
                if p==0:
                    print('all books are issued')
                else:
                    p=p-1
                    print('your '+str(p2)+' book is issued')
            elif b==2:
                if c==0:
                    print('all books are issued')
                else:
                    c=c-1
                    print('your '+str(c2)+' book is issued')
            else:
                if m==0:
                    print('all books are issued')
                else:
                    m=m-1
                    print('your '+str(m2)+' book is issued')
        elif a==2:
            b=input('enter your book name :')
            if b==str(p2):
                if p==2:
                    print('invalid input')
                else:
                    p=p+1
                    print('your book is successfully returned')
            elif b==str(c2):
                if c==2:
                    print('invalid input')
                else:
                    c=c+1
                    print('your book is successfully returned')
            else:
                if m==2:
                    print('invalid input')
                else:
                    m=m+1
                    print('your book is successfully returned')
        elif a==3:
            b=input('enter book you are replacing: ')
            r=input('enter name of new book: ')
            if b==str(p2):
                p2=str(r)
            elif b==str(c2):
                c2=str(r)
            elif b==str(m2):
                m2=str(r)
            else:
                print('invalid input')
        elif a==4:
            print('   Books   no. of books available')
            print('1)',p2,p)
            print('2)',c2,c)
            print('3)',m2,m)
        else:
            print('invalid input')
        ans=input('enter y to go main menu :')
    else:
        break
        
