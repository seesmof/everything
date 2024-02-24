#pragma warning(disable : 4996)

#include "simc.h"

#define real double
#define NL endl
#define nil 0
#define as(type, str) str
#define trunc(value) long(value)
#define input cin
#define output cout
#define halt exit(EXIT_SUCCESS)
#define round(x) ((((x)-trunc(x))>0.5)?(trunc(x)+1):(trunc(x)))
#define succ(type,x) ((type)((x) + 1))
#define _A(t) _ALFA(t)
#define _ALFA(t) alfa_str(t)

#define formatstr(x,y) setw(y)<<(x)
#define formatfloat(x,y,z) setw(y)<<setprecision(z)<<(x)
#define formatint(x,y) setw(y)<<(x)

bool trace,errtest;
typdiarec diarec;
double resettime,systime;
event ievemax,sysevent;
int itransmax;
array_new<1,evemax,bool> waitevent;
array_new<1,evemax,int> maxevent;
listl userlist;
ptransact trans;
plistt delist,current,future;
plistq quelist;
plistf faclist;
plists stlist;
plisth histlist;
array_new<min_signal,max_signal,plistt> signlist;
array_new<1,evemax,plistt> ass, waitl;
long int v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15;
typtrace tracerec;
ptransact translabel;
double eventall;
ofstream outfile;
ifstream f;
cstring<60> str1,str2;
double ctime1,ctime2,realtime;
double msystime,mrealtime,evespeed;
bool dialogus;

int randseed;

real simc_random()
{
return real(rand())/RAND_MAX;
}


template <int min, int max, typename t>
array_new<min,max,t>::array_new(t* other){
    for (int i=0;i<max+1-min;i++)mem[i]=other[i];
   }

/*template <int min, int max, typename t>
t& array_new<min,max,t>::oator[](int index) }*/

template <int size>
cstring<size>::cstring(){
    str[0]=0;
    }
template <int size>
char* cstring<size>::asarray_new(void)	{
    return str;
    }

template<int min, int max>
ostream& operator<<(ostream& os,array_new<min,max,char> a)
{
for (long i=min;i<max;i++) os<<setw(0)<<a[i];
return os;
}

ofstream& operator<<(ofstream &os,char* x)
{
while (*x!=0)
{os<<*x; x++;}
return os;
};


template <int size>
ifstream& operator>>(ifstream &is, cstring<size> &str)
{
is>>str.asarray_new();
return is;
}

template <int size>
istream& operator>>(istream &is, cstring<size> &str)
{
is>>str.asarray_new();
return is;
}

template <int size>
ofstream& operator<<(ofstream &os, cstring<size> &str)
{
os<<str.asarray_new();
return os;
}

const char* btos(bool value)
{ return ((value)?"TRUE":"FALSE"); }

alfa alfa_str(char* text) {
   alfa tmp;
   for (int i=1; i<8; i++)
    tmp[i]=0x20;
   int i1=0, i2=1;
   while ((i1<8)&&text[i1])
    tmp[i2++]=text[i1++];
//   tmp[8]=0x00;
   return tmp;
}

real _clock()
{
    return clock()/CLOCKS_PER_SEC;
}

 void closeoutput(void) {
    outfile.close();
 }
 void waitchar(void) {
    cin.get();
    cin.get();
 }

#define SHOW0(x) (x)
#define SHOW(p,x) setprecision(p)<<(x)
void prnhead(void)
{
outfile<<"<HTML>"<<endl;
outfile<<"<meta charset=\"utf-32\">"<<endl;
outfile<<endl;
outfile<<"<HEAD>"<<endl;
outfile<<"<TITLE>Результыты моделирования</TITLE>"<<endl;
outfile<<"</HEAD>"<<endl;
outfile<<endl;
outfile<<"<BODY>"<<endl;
outfile<<endl;
outfile<<"<TABLE width=100%>"<<endl;
outfile<<"<TR>"<<endl;
outfile<<"<TD width=50%>&nbsp;</TD>"<<endl;
outfile<<"<TD width=50%>"<<endl;
outfile<<"<!-- Вывод информации о разработчиках -->"<<endl;
outfile<<"<TABLE align=right width=100% border=3 cellspacing=0 cellpadding=0>"<<endl;
outfile<<"<THEAD>"<<endl;
outfile<<"<TR align=center>"<<endl;
outfile<<"<TH width=70% align=left><B>СИМ-СИ++ v1.2</B></TH>"<<endl;
outfile<<"<TH width=15%><EM>НУ\"ЗП\"</EM></TH>"<<endl;
outfile<<"<TH width=15%><EM>2020</EM></TH>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"</THEAD>"<<endl;
outfile<<"<TR>"<<endl;
outfile<<"<TD colspan=3><NOBR>Ж.К.Каминская</NOBR><BR>"<<endl;
outfile<<"<NOBR>С.Н. Сердюк</NOBR></TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"</TABLE>"<<endl;
outfile<<endl;
outfile<<"</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"</TABLE>"<<endl;}
void prnlt1(plistt& lt)
   {
     {
        listt& with = *lt;
outfile<<"<TABLE width=100% border=0 cellspacing=0 cellpadding=0>"<<endl;
outfile<<"<TR> <TD width=50%>"<<endl;
outfile<<"<TABLE align=left width=100% border=3 cellspacing=0 cellpadding=0>"<<endl;
outfile<<"<THEAD>"<<endl;
outfile<<"<TR align=center>"<<endl;
outfile<<"<TD> Текущая длина </TD> <TD> Mаксимальная длина </TD>" << endl;
outfile<<"</TR> </THEAD>"<<endl;
outfile<<"<TR align=center> <TD> "<<SHOW0(with.p.ll)<<" </TD> <TD> "<<SHOW0(with.p.lm)<<" </TD> </TR>"<<endl;
outfile<<"</TABLE>"<<endl;
outfile<<"</TD> <TD width=50%> </TD> </TABLE>"<<endl;
     }
   }
 void prnlt(plistt& lt)
   {
     int i;
     ptransact t;

     prnlt1(lt);
     {
        listt& with = *lt;

        if (with.first!=nil)
         {
           t=with.first;
outfile<<"<BR>"<<endl;
outfile<<"<TABLE width=100% border=3 cellspacing=0 cellpadding=0>"<<endl;
outfile<<"<THEAD align=center> <TR>"<<endl;
outfile<<"<TD width=12.5%> NUMB. </TD> <TD with=12.5%> PRTY </TD> <TD width=12.5%> EVE </TD> <TD width=12.5%> NEXTTIME </TD> <TD width=12.5%> ANS </TD> <TD width=12.5%> NANS </TD> " <<
                   " <TD width=12.5%> TESTPRTY </TD> <TD width=12.5%> TRANSLIST </TD> </THEAD>" << NL;
           for( i=1; i <= with.p.ll; i ++)
            {
              {
                 transact& with1 = *with.first;

outfile<<"<TR align=center>"<<endl;
outfile<<"<TD> "<<SHOW0(with1.nom)<<" </TD>"<<endl;
outfile<<"<TD> "<<SHOW0(with1.prty+0x00)<<" </TD>"<<endl;
outfile<<"<TD> "<<SHOW0(with1.eve)<<" </TD>"<<endl;
outfile<<"<TD> "<<SHOW(3,with1.nexttime)<<" </TD>"<<endl;
outfile<<"<TD> "<<SHOW0(with1.ans)<<" </TD>"<<endl;
outfile<<"<TD> "<<SHOW0(with1.nans)<<" </TD>"<<endl;
outfile<<"<TD> "<<SHOW0(with1.testprty)<<" </TD>"<<endl;
outfile<<"<TD> "<<with1.translist->p.name<<" </TD>"<<endl;
outfile<<"</TR>"<<endl;

outfile<<"<TR>"<<endl;
outfile<<"<TD colspan=8> Параметры: <BR>"<<endl;
outfile<<"&nbsp;PI: "<<SHOW0(with1.pi[1])<<' '<<SHOW0(with1.pi[2])<<' '<<SHOW0(with1.pi[3])<<" <BR>"<<endl;
outfile<<"&nbsp;PR: "<<SHOW(3,with1.pr[1])<<' '<<SHOW(3,with1.pr[2])<<' '<<SHOW(3,with1.pr[3])<<" <BR>"<<endl;
outfile<<"&nbsp;PB: "<<btos(with1.pb[1])<<' '<<btos(with1.pb[2])<<" <BR>"<<endl;
outfile<<"&nbsp;PQ: ";
                  if (with1.pq[1]!=nil)
outfile << with1.pq[1]->name; else
outfile << "NIL";
                 if (with1.pq[2]!=nil)
outfile << ' '<<with1.pq[2]->name <<"<BR>"<< NL; else
outfile << " NIL" <<"<BR>"<< NL;
outfile << "&nbsp;PF: ";
                 if (with1.pf[1]!=nil)
outfile << with1.pf[1]->name; else
outfile << "NIL";
                     if (with1.pf[2]!=nil)
outfile << ' '<<with1.pf[2]->name <<"<BR>"<< NL; else
outfile << " NIL"<<"<BR>"<< NL;
outfile << "&nbsp;PS: ";
                 if (with1.ps[1]!=nil)
outfile << with1.ps[1]->name; else
outfile << "NIL";
                 if (with1.ps[2]!=nil)
outfile << ' '<<with1.ps[2]->name <<"<BR>"<< NL; else
outfile << " NIL" <<"<BR>"<< NL;
outfile<<"</TD> </TR>"<<endl;
              }
              with.first=with.first->sled;
            }
           with.first=t;
         }
     }
outfile<<"</TABLE>"<<endl;
   }

// void prnhist(phistogram hist);
 static void printgraf(phistogram& hist);

const int linelength = 111;

const int midleline = 2;


typedef array_new<1,5,char> array_new5;
typedef array_new<1,linelength,char> array_newl;


static void fillpacked(array_newl& a,
                         array_new5 fild5)
  {
    int i,
    j;



    for( i=0; i <= 21; i ++)
     for( j=1; j <= 5; j ++)
      a[i*5+j]=fild5[j];
    a[linelength]=fild5[1];
  }

char bmp_filename[256];
namespace bmp {
#define BITMAP_WIDTH 4
#define BITMAP_HEIGHT 5
#define BITMAP_SIZE 0
#define BITMAP_COLOR unsigned char
#define BITMAP_BLUE 4
#define BITMAP_GREEN 2
#define BITMAP_RED 15
#define BITMAP_BLACK 0
#define BITMAP_WHITE 255
#define BITMAP_DIGIT_SIZE 6
#define BITMAP_DIGIT_DELTA 3
long head[269]= {-1,0,1078,40,-1,-1,524289,0,4,0,0,0,0,0,8388608,32768,8421376,128,8388736,32896,
12632256,12639424,10930928,4202496,6299648,8396800,10493952,12591104,14688256,16384,2113536,4210688,6307840,8404992,10502144,12599296,14696448,24576,2121728,4218880,
6316032,8413184,10510336,12607488,14704640,32768,2129920,4227072,6324224,8421376,10518528,12615680,14712832,40960,2138112,4235264,6332416,8429568,10526720,12623872,
14721024,49152,2146304,4243456,6340608,8437760,10534912,12632064,14729216,57344,2154496,4251648,6348800,8445952,10543104,12640256,14737408,64,2097216,4194368,
6291520,8388672,10485824,12582976,14680128,8256,2105408,4202560,6299712,8396864,10494016,12591168,14688320,16448,2113600,4210752,6307904,8405056,10502208,12599360,
14696512,24640,2121792,4218944,6316096,8413248,10510400,12607552,14704704,32832,2129984,4227136,6324288,8421440,10518592,12615744,14712896,41024,2138176,4235328,
6332480,8429632,10526784,12623936,14721088,49216,2146368,4243520,6340672,8437824,10534976,12632128,14729280,57408,2154560,4251712,6348864,8446016,10543168,12640320,
14737472,128,2097280,4194432,6291584,8388736,10485888,12583040,14680192,8320,2105472,4202624,6299776,8396928,10494080,12591232,14688384,16512,2113664,4210816,
6307968,8405120,10502272,12599424,14696576,24704,2121856,4219008,6316160,8413312,10510464,12607616,14704768,32896,2130048,4227200,6324352,8421504,10518656,12615808,
14712960,41088,2138240,4235392,6332544,8429696,10526848,12624000,14721152,49280,2146432,4243584,6340736,8437888,10535040,12632192,14729344,57472,2154624,4251776,
6348928,8446080,10543232,12640384,14737536,192,2097344,4194496,6291648,8388800,10485952,12583104,14680256,8384,2105536,4202688,6299840,8396992,10494144,12591296,
14688448,16576,2113728,4210880,6308032,8405184,10502336,12599488,14696640,24768,2121920,4219072,6316224,8413376,10510528,12607680,14704832,32960,2130112,4227264,
6324416,8421568,10518720,12615872,14713024,41152,2138304,4235456,6332608,8429760,10526912,12624064,14721216,49344,2146496,4243648,6340800,8437952,10535104,16776176,
10526884,8421504,16711680,65280,16776960,255,16711935,65535,16777215};
BITMAP_COLOR* body;
long width, height, bodysize;
short delta;
const char* digits[10] = {"1111110","1100000","1011011","0011111","0101101","0110111","1110111","0011100","1111111","01111111"};

void setwidth(long w) {
    width=w;
   head[BITMAP_WIDTH]=width;
   }
void setheight(long h) {
    height=h;
   head[BITMAP_HEIGHT]=height;
   }
void create_body(void) {
    delta=0;
   bodysize=(width+delta)*height;
    body=new BITMAP_COLOR[bodysize];
   memset(body,0xff,bodysize);
   for (int j=0; j<height; j++)
        for (int k=0; k<delta; k++)
        body[j*(width+delta)+width+k]=0x00;
    }
void setpixel(int x,int y, BITMAP_COLOR col) {
   body[(height-1-y)*(width+delta)+x]=col;
   }
void line(int x1, int y1, int x2, int y2, BITMAP_COLOR col, int width = 1) {
#define SWAP(x,y) tmp=x,x=y,y=tmp
    int tmp;
   if (x1!=x2) {
      if (x2<x1)
        SWAP(x1,x2),SWAP(y1,y2);
      double stepy=(y2-y1)/double(x2-x1),cy=y1;
      for (int i=x1; i<x2; i++) {
        setpixel(i,cy,col);
         if (width>1)
            setpixel(i,cy-1,col);
         if (width>2)
            setpixel(i,cy+1,col);
         cy+=stepy;
         }
      return;
      }
   if (y1!=y2) {
      if (y2<y1)
        SWAP(x1,x2),SWAP(y1,y2);
      double stepx=(x2-x1)/double(y2-y1),cx=x1;
      for (int j=y1; j<y2; j++) {
        setpixel(cx,j,col);
         if (width>1)
            setpixel(cx-1,j,col);
         if (width>2)
            setpixel(cx+1,j,col);
         cx+=stepx;
         }
      return;
      }
   }

void adddigit(char ch, int x, int y, BITMAP_COLOR col) {
   int ind=ch-0x30;
   if ((ind<0)||(ind>9))
    return;
// type=false - up, type=true - left
#define DRAW(index,deltax,deltay,type) \
    if (digits[ind][index]=='1') \
    line(x+(deltax),y+(deltay),x+(deltax)+((type)?(BITMAP_DIGIT_SIZE):0),y+(deltay)-((type)?0:(BITMAP_DIGIT_SIZE)),col);
   DRAW(0,0,0,false);
   DRAW(1,0,-BITMAP_DIGIT_SIZE,false);
   DRAW(2,0,-2*BITMAP_DIGIT_SIZE,true);
   DRAW(3,BITMAP_DIGIT_SIZE,-BITMAP_DIGIT_SIZE,false);
   DRAW(4,BITMAP_DIGIT_SIZE,0,false);
   DRAW(5,0,0,true);
   DRAW(6,0,-BITMAP_DIGIT_SIZE,true);
   }

void drawtext(int x,int y,long val,BITMAP_COLOR col) {
   char text[256];
   // itoa(val,text,10);
   sprintf(text, "%ld", val);
   int cnt=0,w=0;
   for (;text[cnt];w+=((text[cnt]=='1')?BITMAP_DIGIT_DELTA:(BITMAP_DIGIT_SIZE+BITMAP_DIGIT_DELTA)),cnt++);
   if (!cnt)
    cnt=1, w=(text[cnt]=='1')?BITMAP_DIGIT_DELTA:(BITMAP_DIGIT_SIZE+BITMAP_DIGIT_DELTA);
   w-=BITMAP_DIGIT_DELTA;
   x-=w/2;
   for (int i=0; text[i]; i++) {
      adddigit(text[i],x,y,col);
        if (text[i]!='1')
        x+=BITMAP_DIGIT_SIZE;
      x+=BITMAP_DIGIT_DELTA;
      }
   }

void rectangle(int x1, int y1, int x2, int y2, BITMAP_COLOR col) {
    for (int i=x1; i<x2; i++)
      for (int j=y1; j<y2; j++)
        setpixel(i,j,col);
   }

void create(long w, long h) {
   setwidth(w);
   setheight(h);
   create_body();
   }

void save(char* filename) {
   ofstream out(filename,ios::binary);

    out.put('B');
   out.put('M');
   head[BITMAP_SIZE]=bodysize+1078;
   out.write((char*)head,269*4);
   out.write((char*)body,bodysize);
   out.close();
   }

void free(void) {
   delete[]body;
   }
}

static void printtobmp(phistogram& hist) {
    const int width=640, height = 320, minx=20, maxx=620, miny=5, maxy=310-2*BITMAP_DIGIT_SIZE, delta=2;
   bmp::create(640,320);
   bmp::line(minx,miny,minx,maxy,BITMAP_BLACK);
   bmp::line(minx,maxy,maxx,maxy,BITMAP_BLACK);
   bmp::line(maxx,maxy,maxx,miny,BITMAP_BLACK);
   bmp::line(maxx,miny,minx,miny,BITMAP_BLACK);
   histogram& with = *hist;
   int stepval=(with.maxx-with.minx)/(with.ihint-1);
   real stepgraph=real(maxx-minx)/(with.ihint-1);
   real maxval=0.0,scale;
   for( int i12=1; i12 <= with.ihint; i12 ++)
    if (with.x[i12]>maxval)
         maxval=with.x[i12];
   if (maxval!=0)
    scale=(maxy-miny-3*delta-BITMAP_DIGIT_SIZE*2)/maxval;
   else scale=1;
   for (int i=1; i<with.ihint; i++) {
        bmp::rectangle(minx+(i-1)*stepgraph+delta/2,maxy-scale*with.x[i],minx+i*stepgraph-delta/2,maxy,BITMAP_BLUE);
      bmp::drawtext(minx+(i-1)*stepgraph+stepgraph/2,maxy-scale*with.x[i]-delta,with.x[i],BITMAP_BLACK);
      bmp::drawtext(minx+(i-1)*stepgraph,maxy+delta+2*BITMAP_DIGIT_SIZE,with.minx+(i-1)*stepval,BITMAP_BLACK);
    }
   bmp::drawtext(minx+(with.ihint-1)*stepgraph,maxy+delta+2*BITMAP_DIGIT_SIZE,with.minx+(with.ihint-1)*stepval,BITMAP_BLACK);
   const char* ext = ".BMP";
   const char* pred = "HIST_";
   strcpy(bmp_filename,pred);
   {
    int i=5;
    for (int j=1; with.name[j]&&(j<=8); bmp_filename[i]=with.name[j], i++, j++);
      bmp_filename[i]=0x00;
   }
   strcat(bmp_filename,ext);

   bmp::save(bmp_filename);
   return;
    }

static void printgraf(phistogram& hist)
  {
outfile<<"<BR>"<<endl;
    printtobmp(hist);
outfile<<"<IMG SRC=\""<<bmp_filename<<"\" align=center width=100% alt=\"Гистограмма\">"<<endl;
/*    array_newl workline,
    board,
    midle,
    limiter;
    real xmaxi,
    scale,
    xprint,
    step;
    int i12,
    lineno,
    intervalno,
    position,
    minpos,
    maxpos,
    swap;


    fillpacked(board,as(array_new5,"+----"));
    fillpacked(midle,as(array_new5,".    "));
    midle[1]='I';
    midle[linelength]='I';
    fillpacked(limiter,as(array_new5,"+...."));
    {
       histogram& with = *hist;

       step=(with.maxx-with.minx)/(with.ihint-1);
       xprint=with.minx+step;
       lineno=1;
       intervalno=1;
       xmaxi=0;
       for( i12=1; i12 <= with.ihint; i12 ++)
        if (with.x[i12]>xmaxi)
         xmaxi=with.x[i12];
       if (xmaxi!=0)
        scale=100/xmaxi; else
        scale=1;
       do {
        if (lineno==1)
         {
           workline=board;
           for( position=1; position <= trunc(1+with.x[intervalno]*scale); position ++)
            workline[position]='*';
         } else
         if ((lineno % (midleline+1))==0)
          {
            outfile << ' ' << formatfloat(xprint,10,5);
            xprint=xprint+step;
            workline=limiter;
            minpos=with.x[intervalno];
            maxpos=with.x[intervalno+1];
            if (maxpos<minpos)
             {
               swap=minpos;
               minpos=maxpos;
               maxpos=swap;
             }
            for( position=2; position <= trunc((minpos*scale)); position ++)
             workline[position]='.';
            for( position=trunc(1+scale*minpos); position <=
                          trunc(1+scale*maxpos); position ++)
             workline[position]='*';
          } else
          {
            workline=midle;
            for( position=2; position <= trunc(scale*with.x[intervalno]); position ++)
             workline[position]='.';
            workline[trunc(scale*with.x[intervalno]+1)]='*';
          }
        if ((lineno % (midleline+1))==0)
         {
           outfile << workline << NL;
           intervalno=intervalno+1;
         } else
         outfile << formatstr(" ",11) << workline << NL;
        lineno=lineno+1;
       } while (!(lineno>(midleline+1)*(with.ihint-1)));
    } */
  }

 void prnhist(phistogram hist)
   {
     int j,
     k,
     len,
     maxproc;
     real tty64;
     real y,
     h;

     len=15;
outfile<<"<H2 align=center> Гистограмма "<<hist->name<<" </H2>"<<endl;
//     outfile << formatstr(" ****** ",15) << formatstr(hist->name,10) << formatstr("******",15) << NL;
//     outfile << "     ____________________________________" << NL;
     {
        histogram& with = *hist;

outfile<<"<TABLE width=50% border=3 width=100% cellspacing=0 cellpadding=0>"<<endl;
outfile<<"<TR> <TD width=50%> Диапазон измерений </TD> <TD width=50%> "<< SHOW(3,with.minx) << " .. " << SHOW(3,with.maxx) <<"</TD> </TR>" << NL;
outfile<<"<TR> <TD> Общее число входов </TD> <TD> "<< SHOW0(with.total) <<"</TD> </TR>" << NL;
        if (with.total>1)
         {
outfile<<"<TR> <TD> Среднее значение </TD> <TD> "<< SHOW(5,with.sum/with.total)<< "</TD> </TR> "<<endl;
outfile<<"<TR> <TD> Дисперсия </TD> <TD> "<< SHOW(5,(with.sumsqr-with.sum*with.sum/with.total)/(with.total-1))<< "</TD> </TR> "<<endl;
outfile<<"<TR> <TD> Число выходов за интервал слева </TD> <TD> "<<SHOW0(with.x[0])<<" </TD> </TR> "<<endl;
outfile<<"<TR> <TD> Число выходов за интервал справа </TD> <TD> "<<SHOW0(with.x[with.ihint])<<" </TD> </TR> "<<endl;
outfile<<"</TABLE>"<<endl;

//           outfile << formatstr("  :",25) <<
//                           formatfloat(,12,5) << NL;
//         outfile << formatstr(" Число выходов за интервал :",28) <<
//                   formatstr(" слева -",8) << formatint(with.x[0],8) << formatint(" справа -",9) << formatint(with.x[with.ihint],8) << NL;
//           outfile << formatstr("  ",25) << NL;
//           outfile << formatstr(" __________________ ",25) << NL;
outfile<<"<BR>"<<endl;
outfile<<"<TABLE width=100% border=3 width=100% cellspacing=0  cellpadding=0>"<<endl;
outfile<<"<CAPTION> Таблица наблюдений </CAPTION>"<<endl;
           k=1;
           j=1;
           y=with.minx;
           h=(with.maxx-with.minx)/(with.ihint-1);
outfile<<"<TR>"<<endl;
           do {
            while ((j<=(k+2))&&(j<with.ihint))
             {
//               outfile << " " << formatfloat(y,8,4) << " ." << formatfloat(y+h,8,4) << "/" << formatint(with.x[j],6);
outfile<<"<TD width=12.5% align=center> "<<SHOW(4,y)<<" .. "<< SHOW(4,y+h)<<" </TD> <TD width=12.5% align=center> "<<SHOW0(with.x[j])<<" </TD>"<<endl;
               y=y+h;
               j=j+1;
             }
//            outfile << ' ' << NL;
outfile<<"</TR>"<<endl;
            k=k+3;
           } while (!(j==with.ihint));
outfile<<"</TABLE>"<<endl;
/*           maxproc=0;
           for( k=1; k <= with.ihint-1; k ++)
            {
              with.x[k]=trunc((real)(with.x[k])/with.total*100);
              if (maxproc<with.x[k])
               maxproc=with.x[k];
            } */
         } else
outfile<<"</TABLE>"<<endl;
     }
     if (hist->graf)
      {
//        for( k=1; k <= 20; k ++)
//         tty64 = maxproc;
//         outfile << formatint(trunc(k*tty64/20.0),5);
//        outfile << " %" << NL;
        printgraf(hist);
      }
   }
 void prnt1(ptransact t)
   {
outfile<<"<TABLE width=100% border=3 cellspacing=0 cellpadding=0>"<<endl;
outfile<<"<THEAD align=center> <TR>"<<endl;
outfile<<"<TD width=12.5%> NUMB. </TD> <TD with=12.5%> PRTY </TD> <TD width=12.5%> EVE </TD> <TD width=12.5%> NEXTTIME </TD> <TD width=12.5%> ANS </TD> <TD width=12.5%> NANS </TD> " <<
                   " <TD width=12.5%> TESTPRTY </TD> <TD width=12.5%> TRANSLIST </TD> </THEAD>" << NL;
     {
        transact& with = *t, &with1= *t;

//        outfile << formatint(with.nom,6) << formatint(with.prty,6) << formatint(with.eve,7) << formatfloat(with.nexttime,12,3) <<
//                formatint(with.ans,6) << formatint(with.nans,7) << formatstr(btos(with.testprty),10) << formatstr(with.translist->p.name,16) << NL;
outfile<<"<TR align=center>"<<endl;
outfile<<"<TD> "<<SHOW0(with.nom)<<" </TD>"<<endl;
outfile<<"<TD> "<<SHOW0(with.prty+0x00)<<" </TD>"<<endl;
outfile<<"<TD> "<<SHOW0(with.eve)<<" </TD>"<<endl;
outfile<<"<TD> "<<SHOW(3,with.nexttime)<<" </TD>"<<endl;
outfile<<"<TD> "<<SHOW0(with.ans)<<" </TD>"<<endl;
outfile<<"<TD> "<<SHOW0(with.nans)<<" </TD>"<<endl;
outfile<<"<TD> "<<SHOW0(with.testprty)<<" </TD>"<<endl;
outfile<<"<TD> "<<with.translist->p.name<<" </TD>"<<endl;
outfile<<"</TR>"<<endl;

outfile<<"<TR>"<<endl;
outfile<<"<TD colspan=8> Параметры: <BR>"<<endl;
outfile<<"&nbsp;PI: "<<SHOW0(with1.pi[1])<<' '<<SHOW0(with1.pi[2])<<' '<<SHOW0(with1.pi[3])<<" <BR>"<<endl;
outfile<<"&nbsp;PR: "<<SHOW(3,with1.pr[1])<<' '<<SHOW(3,with1.pr[2])<<' '<<SHOW(3,with1.pr[3])<<" <BR>"<<endl;
outfile<<"&nbsp;PB: "<<btos(with1.pb[1])<<' '<<btos(with1.pb[2])<<" <BR>"<<endl;
outfile<<"&nbsp;PQ: ";
                  if (with1.pq[1]!=nil)
outfile << with1.pq[1]->name; else
outfile << "NIL";
                 if (with1.pq[2]!=nil)
outfile << ' '<<with1.pq[2]->name <<"<BR>"<< NL; else
outfile << " NIL" <<"<BR>"<< NL;
outfile << "&nbsp;PF: ";
                 if (with1.pf[1]!=nil)
outfile << with1.pf[1]->name; else
outfile << "NIL";
                     if (with1.pf[2]!=nil)
outfile << ' '<<with1.pf[2]->name <<"<BR>"<< NL; else
outfile << " NIL"<<"<BR>"<< NL;
outfile << "&nbsp;PS: ";
                 if (with1.ps[1]!=nil)
outfile << with1.ps[1]->name; else
outfile << "NIL";
                 if (with1.ps[2]!=nil)
outfile << ' '<<with1.ps[2]->name <<"<BR>"<< NL; else
outfile << " NIL" <<"<BR>"<< NL;
outfile<<"</TD> </TR>"<<endl;
     }
   }

 void prnq(pqueue q)
   {
     real dq;

     { queue& with = *q;
      if (with.ci!=0)
       {
         if (with.ci!=with.co)
          dq=with.timeq/(with.ci-with.co); else dq=0.0;
outfile<<"<TR align=center>"<<endl;
outfile<<"<TH align=left rowspan=2>&nbsp;"<<with.name<<"</TH>"<<endl;
outfile<<"<TD>"<<SHOW0(with.ci)<<"</TD>"<<endl;
outfile<<"<TD>"<<SHOW0(with.mq)<<"</TD>"<<endl;
outfile<<"<TD>"<<SHOW(3,with.mtime)<<"</TD>"<<endl;
outfile<<"<TD rowspan=2>"<<SHOW(3,with.lm)<<"</TD>"<<endl;
outfile<<"<TD rowspan=2>"<<SHOW(3,(real)(with.co)/with.ci*100)<<"</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"<TR align=center>"<<endl;
outfile<<"<TD>"<<SHOW0(with.co)<<"</TD>"<<endl;
outfile<<"<TD>"<<SHOW0(with.lq)<<"</TD>"<<endl;
outfile<<"<TD align=center>"<<SHOW(3,dq)<<"</TD>"<<endl;
outfile<<"</TR>"<<endl;
/*         outfile << formatint(with.name,9) << formatint(with.ci,12) << formatint(with.mq,12) << formatfloat(with.mtime,17,3) << formatfloat(with.lm,11,3) <<
                 formatfloat((real)(with.co)/with.ci*100,10,3) << NL;
         outfile << formatint(with.co,21) << formatint(with.lq,12) << formatfloat(dq,17,3) << NL; */
       } else
       outfile << formatint(with.name,9) << NL;}
   }
 void prns(pstorage st)
   {
     { storage& with = *st;
      if (with.ci!=0)
{
outfile<<"<TR align=center>"<<endl;
outfile<<"<TH align=left>&nbsp;"<<with.name<<"</TH>"<<endl;
outfile<<"<TD>"<<SHOW0(with.s)<<"</TD>"<<endl;
outfile<<"<TD>"<<SHOW(3,with.ut)<<"</TD>"<<endl;
outfile<<"<TD>"<<SHOW0(with.mtime)<<"</TD>"<<endl;
outfile<<"<TD>"<<SHOW0(with.ss)<<"</TD>"<<endl;
outfile<<"<TD>"<<SHOW0(with.sm)<<"</TD>"<<endl;
outfile<<"<TD>"<<SHOW(2,with.smean)<<"</TD>"<<endl;
outfile<<"<TD>"<<SHOW0(with.ci)<<"</TD>"<<endl;
outfile<<"</TR>"<<endl;
//       outfile << formatint(with.name,9) << formatint(with.s,12) << formatfloat(with.ut,10,3) << formatfloat(with.mtime,16,3) <<
//formatint(with.ss,10) << formatint(with.sm,11) <<
//                         formatfloat(with.smean,11,3) << formatint(with.ci,8) << NL; else
//       outfile << formatint(with.name,9) << formatint(with.s,12) << NL;
}
     }

   }
 void prnf(pfacility f)
   {
     { facility& with = *f;
      if (with.ci!=0)
       {
outfile<<"<TR align=center>"<<endl;
outfile<<"<TH align=left>&nbsp;"<<with.name<<"</TH>"<<endl;
outfile<<"<TD>"<<SHOW0(with.ci)<<"</TD>"<<endl;
outfile<<"<TD>"<<SHOW(3,with.mtime)<<"</TD>"<<endl;
outfile<<"<TD>"<<SHOW(3,with.pro)<<"</TD>"<<endl;
outfile<<"<TD>"<<SHOW0(with.p)<<"</TD>"<<endl;
outfile<<"<TD>";
//         outfile << formatstr(with.name,9) << formatint(with.ci,9) << formatfloat(with.mtime,19,3) << formatfloat(with.pro,12,3) << formatint(with.p,10);
         switch (with.status) {
          case facility::free:      outfile << "FREE";     break;
          case facility::seized:    outfile << "SEIZED";     break;
          case facility::preempted: outfile << "PREEMPTED"; break;
         }
       } else
outfile << formatstr(with.name,9);
outfile<<"</TD>"<<endl;
outfile<<"</TR>"<<endl;
       }

   }

 void prwaitl()
   {
     int i;

     for( i=1; i <= evemax; i ++)
      if (waitl[i]!=nil)
       {
outfile << "<H2> Системный список "<<formatstr(" WAITL",14) << formatint(i,5) <<"</H2>"<< NL;
         prnlt(waitl[i]);
       }
   }

 void prnuserlt()
   {
     int i;

      for( i=1; i <= userlist.ll; i ++)
       {
//         outfile << "     " << userlist.first->p.name << NL;
outfile << "<H2> Пользовательский список "<<userlist.first->p.name<< " </H2>"<< NL;

         prnlt(userlist.first);
         userlist.first=userlist.first->sled;
       }
   }

 void lfprint(plistf lf)
   {
     int i;

     { listf& with = *lf;
      if (with.first!=nil)
       for( i=1; i <= with.p.ll; i ++)
        {
outfile << "<H2 align=center>Список прибора " << with.first->name << "</H2>"<<NL;
          prnlt(with.first->fl);
          if (with.first->inter!=nil)
           {
outfile << "<H2 align=center>Список прерванных транзактов " << with.first->name << "</H2>"<<NL;
             prnlt(with.first->inter);
           }
          with.first=with.first->sled;
        }}
   }

 void lsprint(plists ls)
   {
     int i;

     { lists& with = *ls;
      if (with.first!=nil)
       for( i=1; i <= with.p.ll; i ++)
        {
outfile << "<H2 align=center>Список накопителя " << with.first->name << "<BR>"<<NL;
          prnlt(with.first->slt);
          with.first=with.first->sled;
        }}
   }

 void prnlq(plistq lq)
   {
     int i;

outfile<<"<!-- Вывод информации об очередях-->"<<endl;
outfile<<"<BR>"<<endl;
outfile<<"<TABLE border=3 width=100% cellspacing=0 cellpadding=0>"<<endl;
outfile<<"<CAPTION>Очереди</CAPTION>"<<endl;
outfile<<"<THEAD>"<<endl;
outfile<<"<TR align=center>"<<endl;
outfile<<"<TH align=left width=20% rowspan=2>&nbsp;Очередь</TH>"<<endl;
outfile<<"<TD width=16%>Число входов</TD>"<<endl;
outfile<<"<TD width=16%>Макс. длина</TD>"<<endl;
outfile<<"<TD width=16%>Ср. вр. ож.</TD>"<<endl;
outfile<<"<TD width=16% rowspan=2>Средняя длина</TD>"<<endl;
outfile<<"<TD width=16% rowspan=2>% вх. в пустую оч.</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"<TR align=center>"<<endl;
outfile<<"<TD>С 0 вр. ож.</TD>"<<endl;
outfile<<"<TD>Текущ.длина</TD>"<<endl;
outfile<<"<TD>Без уч. 0 вх.</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"</THEAD>"<<endl;

     { listq& with = *lq;
      for( i=1; i <= with.p.ll; i ++)
       {
         prnq(with.first);
         with.first=with.first->sled;
       }}
outfile<<"</TABLE>"<<endl;
   }

 void prnls(plists ls)
   {
     int i;

outfile<<"<!-- Вывод информации о накопителях-->"<<endl;
outfile<<"<BR>"<<endl;
outfile<<"<TABLE width=100% border=3 cellspacing=0 cellpadding=0>"<<endl;
outfile<<"<CAPTION>Накопители</CAPTION>"<<endl;
outfile<<"<THEAD align=center>"<<endl;
outfile<<"<TR>"<<endl;
outfile<<"<TH rowspan=2 align=left width=20%>&nbsp;Накопитель</TH>"<<endl;
outfile<<"<TD rowspan=2 width=8%>Емк.</TD>"<<endl;
outfile<<"<TD rowspan=2 width=8%>Загр.</TD>"<<endl;
outfile<<"<TD rowspan=2 width=16%>Ср. время пребывания</TD>"<<endl;
outfile<<"<TD colspan=3>Содержимое</TD>"<<endl;
outfile<<"<TD rowspan=2 width=16%>Число входов</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"<TR>"<<endl;
outfile<<"<TD>Текущ.</TD>"<<endl;
outfile<<"<TD>Макс.</TD>"<<endl;
outfile<<"<TD>Сред.</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"</THEAD>"<<endl;

     { lists& with = *ls;
      for( i=1; i <= with.p.ll; i ++)
       {
         prns(with.first);
         with.first=with.first->sled;
       }}
outfile<<"</TABLE>"<<endl;
   }

 void prnlf(plistf lf)
   {
     int i;

outfile<<"<!-- Вывод информации о приборах -->"<<endl;
outfile<<"<BR>"<<endl;
outfile<<"<TABLE width=100% border=3 cellspacing=0 cellpadding=0>"<<endl;
outfile<<"<CAPTION>Приборы</CAPTION>"<<endl;
outfile<<"<THEAD align=center>"<<endl;
outfile<<"<TR>"<<endl;
outfile<<"<TH align=left width=20%>&nbsp;Прибор</TH>"<<endl;
outfile<<"<TD width=16%>Число входов</TD>"<<endl;
outfile<<"<TD width=16%>Ср. время обработки</TD>"<<endl;
outfile<<"<TD width=16%>Загрузка</TD>"<<endl;
outfile<<"<TD width=16%>Число захватов</TD>"<<endl;
outfile<<"<TD width=16%>Состояние</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"</THEAD>"<<endl;

     { listf& with = *lf;
      for( i=1; i <= with.p.ll; i ++)
       {
         prnf(with.first);
         with.first=with.first->sled;
       }}
outfile<<"</TABLE>"<<endl;
   }

 void prnlh(plisth lh)
   {
     int i;

     { listh& with = *lh;
      for( i=1; i <= with.p.ll; i ++)
       {
         prnhist(with.first);
         with.first=with.first->sled;
       }}
   }

 void prnq1(pqueue que)
   {
outfile<<"<!-- Вывод информации об очередях-->"<<endl;
outfile<<"<BR>"<<endl;
outfile<<"<TABLE border=3 width=100% cellspacing=0 cellpadding=0>"<<endl;
outfile<<"<CAPTION>Очереди</CAPTION>"<<endl;
outfile<<"<THEAD>"<<endl;
outfile<<"<TR align=center>"<<endl;
outfile<<"<TH align=left width=20% rowspan=2>&nbsp;Очередь</TH>"<<endl;
outfile<<"<TD width=16%>Число входов</TD>"<<endl;
outfile<<"<TD width=16%>Макс. длина</TD>"<<endl;
outfile<<"<TD width=16%>Ср. вр. ож.</TD>"<<endl;
outfile<<"<TD width=16% rowspan=2>Средняя длина</TD>"<<endl;
outfile<<"<TD width=16% rowspan=2>% вх. в пустую оч.</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"<TR align=center>"<<endl;
outfile<<"<TD>С 0 вр. ож.</TD>"<<endl;
outfile<<"<TD>Текущ.длина</TD>"<<endl;
outfile<<"<TD>Без уч. 0 вх.</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"</THEAD>"<<endl;
        prnq(que);
outfile<<"</TABLE>"<<endl;
   }

 void prnf1(pfacility fac)
   {
outfile<<"<!-- Вывод информации о приборах -->"<<endl;
outfile<<"<BR>"<<endl;
outfile<<"<TABLE width=100% border=3 cellspacing=0 cellpadding=0>"<<endl;
outfile<<"<CAPTION>Приборы</CAPTION>"<<endl;
outfile<<"<THEAD align=center>"<<endl;
outfile<<"<TR>"<<endl;
outfile<<"<TH align=left width=20%>&nbsp;Прибор</TH>"<<endl;
outfile<<"<TD width=16%>Число входов</TD>"<<endl;
outfile<<"<TD width=16%>Ср. время обработки</TD>"<<endl;
outfile<<"<TD width=16%>Загрузка</TD>"<<endl;
outfile<<"<TD width=16%>Число захватов</TD>"<<endl;
outfile<<"<TD width=16%>Состояние</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"</THEAD>"<<endl;
     prnf(fac);
outfile<<"</TABLE>"<<endl;
   }

 void prns1(pstorage st)
   {
outfile<<"<!-- Вывод информации о накопителях-->"<<endl;
outfile<<"<BR>"<<endl;
outfile<<"<TABLE width=100% border=3 cellspacing=0 cellpadding=0>"<<endl;
outfile<<"<CAPTION>Накопители</CAPTION>"<<endl;
outfile<<"<THEAD align=center>"<<endl;
outfile<<"<TR>"<<endl;
outfile<<"<TH rowspan=2 align=left width=20%>&nbsp;Накопитель</TH>"<<endl;
outfile<<"<TD rowspan=2 width=8%>Емк.</TD>"<<endl;
outfile<<"<TD rowspan=2 width=8%>Загр.</TD>"<<endl;
outfile<<"<TD rowspan=2 width=16%>Ср. время пребывания</TD>"<<endl;
outfile<<"<TD colspan=3>Содержимое</TD>"<<endl;
outfile<<"<TD rowspan=2 width=16%>Число входов</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"<TR>"<<endl;
outfile<<"<TD>Текущ.</TD>"<<endl;
outfile<<"<TD>Макс.</TD>"<<endl;
outfile<<"<TD>Сред.</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"</THEAD>"<<endl;
     prns(st);
outfile<<"</TABLE>"<<endl;
   }

 void prnh1(phistogram hist)
   {
     hist->graf=false;
     prnhist(hist);
   }

 void printall()
   {
     const char stars1[] = "                       *****************************";
     const char stars2[] = "                       *                           *";
     event i,
     j,
     k;
     ofstream g;


   if (trace)
   outfile<<"</TABLE>"<<endl;


outfile<<"<BR>"<<endl;
outfile<<"<TABLE width=50% border=3 cellspacing=0 cellpadding=3>"<<endl;
outfile<<"<CAPTION align=center>&nbsp;Общие параметры среды:&nbsp;</CAPTION>"<<endl;
outfile<<"<TR width=50%> <TD>Текущее время</TD> <TD width=50%>"<<SHOW(3,systime)<<"</TD> </TR>"<<endl;
outfile<<"<TR> <TD>Текущее событие</TD> <TD>"<<SHOW0(sysevent)<<"</TD> </TR>"<<endl;
if (trans==nil)
    outfile<<"<TR> <TD>Текущий транзакт</TD> <TD>NIL</TD> </TR>"<<endl;
   else outfile<<"<TR> <TD>Текущий транзакт</TD> <TD>"<<SHOW0(trans->nom)<<"</TD> </TR>"<<endl;
outfile<<"<TR> <TD>Всего событий</TD> <TD>"<<SHOW0(eventall)<<"</TD> </TR>"<<endl;
outfile<<"<TR> <TD>Время моделирования</TD> <TD>"<<SHOW(2,realtime)<<" сек.</TD> </TR>"<<endl;
outfile<<"<TR> "<<endl;
outfile<<"<TD>Среднее время выполнения события</TD>"<<endl;
if (realtime==0.0)
    outfile<<"<TD>"<<SHOW(5,realtime)<<" сек/событие</TD>"<<endl;
   else outfile<<"<TD>"<<SHOW(5,realtime/eventall)<<" сек/событие</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"</TABLE>"<<endl;

    ievemax=evemax;
   while (((maxevent[ievemax]==0) && (ievemax>5))==true)
    ievemax--;

outfile<<"<!-- Вывод количества событий -->"<<endl;
for (int i=0; i<(((ievemax%10)==0)?(ievemax/10):(ievemax/10 + 1)); i++)
{
    int segm=i*10;
outfile<<"<BR>"<<endl;
outfile<<"<TABLE border=3 width=100% cellspacing=0 cellpadding=0>"<<endl;
outfile<<"<TR align=center>"<<endl;
outfile<<"<TH width=20% align=left>&nbsp;СОБЫТИЕ</TH>"<<endl;
    for (int j=1; j<=10; j++)
outfile<<"<TD width=8%>"<<SHOW0(segm+j)<<"</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"<TR align=center>"<<endl;
outfile<<"<TH align=left>&nbsp;ВСЕГО</TH>"<<endl;
    for (int j=1; j<=10; j++)
    if (segm+j<=ievemax)
outfile<<"<TD>"<<SHOW0(maxevent[segm+j])<<"</TD>"<<endl;
        else
outfile<<"<TD>&nbsp;</TD>"<<endl;


outfile<<"</TR>"<<endl;
outfile<<"</TABLE>"<<endl;
}

     if (quelist->first!=nil)
      {
/*        outfile << stars1 << NL;
        outfile << stars2 << NL;
        outfile << formatstr(" ",15) << "        *  -----   Очереди   -----  *" << NL;
        outfile << stars2 << NL;
        outfile << stars1 << NL;
        outfile << NL; */
        prnlq(quelist);
//        outfile << NL;
      }
     if (faclist->first!=nil)
      {
/*        outfile << stars1 << NL;
        outfile << stars2 << NL;
        outfile << formatstr(" ",15) << "        *  ----    Приборы    ----  *" << NL;
        outfile << stars2 << NL;
        outfile << stars1 << NL;
        outfile << NL; */
        prnlf(faclist);
//        outfile << NL;
      }
     if (stlist->first!=nil)
      {
/*        outfile << stars1 << NL;
        outfile << stars2 << NL;
        outfile << formatstr(" ",15) << "        *  ----   Накопители  ----  *" << NL;
        outfile << stars2 << NL;
        outfile << stars1 << NL;
        outfile << NL; */
        prnls(stlist);
//        outfile << NL;
      }
     if (userlist.first!=nil)
      {
/*        outfile << stars1 << NL;
        outfile << stars2 << NL;
        outfile << formatstr(" ",15) << "        *     Списки пользователя   *" << NL;
        outfile << stars2 << NL;
        outfile << stars1 << NL;
        outfile << NL; */
        prnuserlt();
//        outfile << NL;
      }
     if (histlist->first!=nil)
      {
/*        outfile << stars1 << NL;
        outfile << stars2 << NL;
        outfile << formatstr(" ",15) << "        *  ----  Гистограммы  ----  *" << NL;
        outfile << stars2 << NL;
        outfile << stars1 << NL;
        outfile << NL; */
        prnlh(histlist);
//        outfile << NL;
      }
     if (errtest || trace)
      {
//        outfile << stars1 << NL;
//        outfile << stars2 << NL;
outfile<<"<H1 align=center>Системные списки</H1>" << NL;
//        outfile << stars2 << NL;
//        outfile << stars1 << NL;
//        outfile << NL;
outfile << "<H2 align=center>Список CURRENT</H2>" << NL;
        prnlt(current);
        prwaitl();
        lfprint(faclist);
        lsprint(stlist);
outfile << "<H2 align=center>Список FUTURE</H2>" << NL;
        prnlt(future);
        for( i=1; i <= evemax; i ++)
         if (ass[i]!=nil)
          {
            outfile << "     ASSEMBLE" << formatint(i,6) << NL;
            prnlt(ass[i]);
          }
        outfile << NL;
      }
   }

void starttrace(void)
{
if (trace)
    return;
outfile<<"<!-- Вывод трассировки -->"<<endl;
outfile<<"<BR>"<<endl;
outfile<<"<TABLE border=3 width=100% cellspacing=0  cellpadding=0>"<<endl;
outfile<<"<CAPTION>Трассировка</CAPTION>"<<endl;
outfile<<"<THEAD>"<<endl;
outfile<<"<TR>"<<endl;
outfile<<"<TD width=10%>&nbsp;№ соб&nbsp;</TD>"<<endl;
outfile<<"<TD width=10%>&nbsp;Сис. время&nbsp;</TD>"<<endl;
outfile<<"<TD width=70%>&nbsp;Описание&nbsp;</TD>"<<endl;
outfile<<"</TR>"<<endl;
outfile<<"</THEAD>"<<endl;
trace=true;
}
void stoptrace(void)
{
if (!trace)
    return;
outfile<<"</TABLE"<<endl;
trace=false;
}

 void tracer(int tracecode)
   {
     const char tr[] = "  Транзакт ";
     const char fa[] = "  прибор ";
     const char ne[] = "  NextTime=";

if (tracecode==0)
    return;

outfile<<"<TR align=center>"<<endl;
outfile<<"<TD>"<<SHOW0(sysevent)<<"</TD>"<<endl;
outfile<<"<TD>"<<SHOW(2,systime)<<"</TD>"<<endl;
outfile<<"<TD align=left>";



     //outfile << formatint(sysevent,5) << ": ";
      switch (tracecode) {
       case 1: outfile << ' '<< tr << ' '<<SHOW0(tracerec.t->nom) << " помещен в модель (EVE=" << SHOW0(tracerec.t->eve) <<","<<
                    ne << SHOW(2,tracerec.t->nexttime) <<")."<< NL;
                  break;
       case 2: outfile << " Создан" << tr << ' '<<SHOW0(tracerec.t->nom) << " (EVE=" << SHOW0(tracerec.t->eve) << ','<< ne << SHOW(2,tracerec.t->nexttime) << ")." << NL; break;
       case 3: outfile << " Уничтожен" << tr << ' '<<SHOW0(trans->nom) << NL; break;
       case 4: outfile << tr <<' '<< SHOW0(trans->nom) << " задержен на " << SHOW(3,tracerec.r) << " ("<<ne <<
                  SHOW(3,trans->nexttime) <<")."<< NL;
                  break;
       case 5: outfile << tr << formatint(trans->nom,5) << "  Eve=" << formatint(trans->eve,4) <<
                  "   помещен в список Waitl[" << formatint(tracerec.e,4) << ']' << NL;
                  break;
       case 6: outfile << tr << formatint(trans->nom,5) <<
                  "   направлен на выполнение события" << formatint(tracerec.e,5) << NL;
                  break;
       case 7: outfile << tr << formatint(trans->nom,5) << " пытался захватить" << fa <<
                  formatstr(tracerec.f->name,9) << ", занимаемый" << tr << "ом " << formatint(tracerec.f->transpoint->nom,5) << NL;
                  break;
       case 8: outfile << fa << formatstr(tracerec.f->name,9) << " захвачен" << tr << "ом" << formatint(trans->nom,5) <<
                  " обработка" << tr << 'а' << formatint(tracerec.f->transpoint->nom,5) << " прервана" << NL;
                  break;
       case 9: outfile << tr << formatint(trans->nom,5) << "  занял " <<fa << formatstr(tracerec.f->name,9) << NL; break;
      case 10: outfile << tr << formatint(trans->nom,5) << "  освободил " <<fa << formatstr(tracerec.f->name,9) << NL; break;
      case 11: outfile << tr << formatint(tracerec.f->transpoint->nom,5) <<
                  " возвращен в" << fa << formatstr(tracerec.f->name,9) << " на дообработку" << NL;
                  break;
      case 12: outfile << tr << formatint(trans->nom,5) << " покинул очередь " << formatstr(tracerec.q->name,9) << NL; break;
      case 13: outfile << tr << formatint(trans->nom,5) << " встал в очередь " << formatstr(tracerec.q->name,9) << NL; break;
      case 14: outfile << tr << formatint(trans->nom,5) << " пытался занять" << fa << formatstr(tracerec.f->name,9) << NL; break;
      case 15: outfile << tr << formatint(trans->nom,5) << "  занял" << fa << formatstr(tracerec.f->name,9) << NL; break;
      case 16: outfile << tr << formatint(trans->nom,6) << "  занял" << formatint(tracerec.n,4) <<
                  " ячеек в накопителе " << formatstr(tracerec.s->name,9) << NL;
                  break;
      case 17: outfile << tr << formatint(trans->nom,6) << " пытался войти в накопитель " << formatstr(tracerec.s->name,9) << NL; break;
      case 18: outfile << tr << formatint(trans->nom,6) << " освободил" << formatstr(tracerec.n,5) <<
                  " ячеек накопителя " << formatstr(tracerec.s->name,9) << NL;
                  break;
      case 19: outfile << tr << formatint(tracerec.t->nom,6) << " переведен из списка накопителя в Current" << NL; break;
      case 20: outfile << " Параметру "; break;
     case 201: outfile << "PI["; break;
     case 202: outfile << "PB["; break;
     case 203: outfile << "PR["; break;
     case 204: outfile << "PF["; break;
     case 205: outfile << "PQ["; break;
     case 206: outfile << "PS["; break;
     case 207: outfile << formatint(tracerec.n,2) << "] всех членов ансамбля " << formatint(trans->ans,5) <<
                " присвоено значение ";
                break;
     case 208: outfile << trans->pi[tracerec.n]; break;
     case 209: outfile << formatstr(btos(trans->pb[tracerec.n]),7); break;
     case 210: outfile << trans->pr[tracerec.n]; break;
     case 211: outfile << '^' << formatstr(trans->pf[tracerec.n]->name,9); break;
     case 212: outfile << '^' << formatstr(trans->pq[tracerec.n]->name,9); break;
     case 213: outfile << '^' << formatstr(trans->ps[tracerec.n]->name,9); break;
     case 214: {
            outfile << NL;
            outfile << "  Hомер  Prty   Eve   NextTime    Ans    NAns" <<
                    "    TestPrty    TransList" << NL;
          }
          break;
      case 21: { transact& with1 = *tracerec.t;
           outfile << formatint(with1.nom,6) << formatint(with1.prty,6) << formatint(with1.eve,7) << formatfloat(with1.nexttime,12,3) << formatint(with1.ans,6) <<
                   formatint(with1.nans,7) << formatstr(btos(with1.testprty),10) << formatint(with1.translist->p.name,16) << NL;}
                   break;
      case 22: outfile << " Для" << tr << 'а' << formatint(trans->nom,5) << ", ансамбль" << formatint(trans->ans,5) <<
                  " создано" << formatint(tracerec.n,4) << " потомков," <<
                  " которые направлены по адресу" << formatint(tracerec.e,6) << NL;
                  break;
      case 23: outfile << " Начат сбор членов ансамбля" << formatint(trans->ans,5) <<
                  " в событии" << formatint(sysevent,6) << NL;
                  break;
      case 24: outfile << tr << formatint(trans->nom,5) << ", ансамбль" << formatint(trans->ans,5) <<
                  " выведен из модели в событии" << formatint(sysevent,6) << NL;
                  break;
      case 25: outfile << " Закончен сбор членов ансамбля" << formatint(trans->ans,5) <<
                  " в событии" << formatint(sysevent,6) << NL;
                  break;
      case 26: {
            outfile << " Всем членам ансамбля" << formatint(trans->ans,5) <<
                    " установлен приоритет" << formatint(trans->prty,4) << NL;
            output << "  Номер  Prty   Eve   NextTime    Ans    NAns" <<
                    "    TestPrty    TransList" << NL;
          }
          break;
      case 27: { transact& with1 = *tracerec.t;
           outfile << formatint(with1.nom,6) << formatint(with1.prty,6) << formatint(with1.eve,7) << formatfloat(with1.nexttime,12,3) << formatint(with1.ans,6) <<
                   formatint(with1.nans,7) << formatstr(btos(with1.testprty),10) << formatstr(tracerec.t->translist->p.name,16) << NL;}
                   break;
      case 28: outfile << tr << formatint(trans->nom,5) << " помещен в список SignList" <<
                  formatint(tracerec.n,4) << NL;
                  break;
      case 29: outfile << tr << "ы, ожидавшие сигнала" << formatint(tracerec.n,4) <<
                  ", переведены в список Current" << NL;
                  break;
      case 30: outfile << " Нет " << tr << "ов, ожидающих сигнала" << formatint(tracerec.n,4) << NL;
      break;
      }
outfile<<"</TD>"<<endl;
outfile<<"</TR>"<<endl;

   }

void error(int errcode);
void error1(int& errcode);

static void errglob()
  {
/*    outfile << formatstr("    ",15) << "        *****************************" << NL;
    outfile << formatstr("    ",15) << "        *                           *" << NL;
    outfile << formatstr("    ",15) << "        *         *" << NL;
    outfile << formatstr("    ",15) << "        *                           *" << NL;
    outfile << formatstr("    ",15) << "        *****************************" << NL; */
outfile<<"<H1> Диагностика ошибок </H1>"<<endl;
  }


static void errmsg(int i,bool b, bool& ok, int& errcode)
  {
    cstring<256> line;
    int j;

    if (b)
     errglob();
/*    assign(f,"SIMPAS.ERR");
    reset(f);
    ok=(ioresult==0);*/
    f.open("SIMPAS.ERR");
    //ok=f;
    if (!f)
     outfile << "<P> Error code #" << formatint(errcode,5) << "</P>" << NL; else
     {
       for( j=1; j <= i; j ++)
        f >> line/* >> NL */;
       outfile << line << NL;
       f.close();
     }
    if (b)
     {
       printall();
       outfile.close();
       halt;
     }
  }


void error1(int& errcode)
  {
    bool ok;

    errtest=true;
     switch (errcode) {
      case 101: errmsg(1,true, ok, errcode); break;
      case 102: errmsg(2,true, ok, errcode); break;
      case 103: errmsg(3,true, ok, errcode); break;
      case 201: errmsg(4,false, ok, errcode); break;
      case 202: errmsg(5,false, ok, errcode); break;
      case 203: errmsg(6,false, ok, errcode); break;
      case 204: errmsg(7,false, ok, errcode); break;
      case 205: errmsg(8,false, ok, errcode); break;
      case 206: errmsg(9,false, ok, errcode); break;
      case 207: errmsg(10,false, ok, errcode); break;
      case 208: errmsg(11,false, ok, errcode); break;
      case 209: errmsg(12,false, ok, errcode); break;
      case 301: errmsg(13,false, ok, errcode); break;
      case 302: errmsg(14,false, ok, errcode); break;
      case 401: errmsg(15,false, ok, errcode); break;
      case 402: errmsg(16,true, ok, errcode); break;
      case 403: errmsg(17,true, ok, errcode); break;
      case 404: errmsg(18,true, ok, errcode); break;
      case 405: errmsg(19,true, ok, errcode); break;
      case 501: errmsg(20,true, ok, errcode); break;
      case 502: errmsg(21,true, ok, errcode); break;
      case 601: errmsg(22,true, ok, errcode); break;
      case 602: errmsg(23,true, ok, errcode); break;
      case 701: errmsg(24,true, ok, errcode); break;
      case 702: errmsg(25,true, ok, errcode); break;
      case 711: errmsg(26,true, ok, errcode); break;
      case 712: errmsg(27,true, ok, errcode); break;
      case 713: errmsg(28,true, ok, errcode); break;
      case 714: errmsg(29,true, ok, errcode); break;
      case 715: errmsg(30,false, ok, errcode); break;
      case 716: errmsg(31,true, ok, errcode); break;
      case 717: errmsg(32,true, ok, errcode); break;
      case 801: errmsg(33,true, ok, errcode); break;
      case 802: errmsg(34,true, ok, errcode); break;
     case 7301: errmsg(35,true, ok, errcode); break;
     case 7302: errmsg(36,true, ok, errcode);
     break;
     }
  }

void error(int errcode)
  {
       outfile<<"<P>В процессе моделирования произошла ошибка #"<<errcode<<" </P>"<<endl;
       outfile<<"<A href=\"error.html\"> Диагностика ошибок </A>"<<endl;
         outfile.close();
//       assign(outfile,"error.rez");
//       rewrite(outfile);
       outfile.open("ERROR.HTML");
       error1(errcode);
       outfile.close();
//       assign(outfile,"tty.err");
//       rewrite(outfile);
//       outfile.open("TTY.HTML");
//       error1(errcode);
  }

real rand01(long int& v)
  {
    real rand01_result;
    randseed=v;
    rand01_result=simc_random();
    v=randseed;
    return rand01_result;
  }

real randexp(real lambda,long int& v)
 /* VAR
    R:REAL;
  BEGIN
    R:=Rand01(V);
    IF R<0.00001 THEN
     R:=0.00001;
    RANDEXP:=-1.0/LAMBDA*LN(R)*/
  {
    v=0;
    real randexp_result;
    randexp_result=lambda*(-log(1-simc_random()));
    return randexp_result;
  }

real randab(real a,real b,long int& v)
  {
    real randab_result;
    randab_result=rand01(v)*(b-a)+a;
    return randab_result;
  }

real randnorm(real xmean,real disp,long int& v)
  {
    real r;

    real randnorm_result;
    r=rand01(v);
    if (r<0.00001)
     r=0.00001;
    randnorm_result=xmean+sqrt(-2.0*log(r)*disp)*cos(6.2831854*rand01(v));
    return randnorm_result;
  }

int randpoisson(real mu,long int& v)
 /* var
    E: real;
    K: int;
  begin
    E:=exp(-Mu);
    K:=0;
    while Rand01(V)>=E do
     K:=K+1;
    RandPoisson:=K  */
  {
    int randpoisson_result;
    randpoisson_result=round(mu*(-log(1-rand01(v))));
    return randpoisson_result;
  }

real randdtable(table t,long int& v)
  {
    unsigned char i;
    real r;

     real randdtable_result;
     {
       i=1;
       r=rand01(v);
       while (t.p[i]<r)  i++;
       randdtable_result=t.x[i];
     }
     return randdtable_result;
  }

real randtable(table t,long int& v)
  {
    unsigned char i;
    real r;

     real randtable_result;
     {
       i=2;
       r=rand01(v);
       if (t.p[1]!=0)
        error(7301);
       while (t.p[i]<r)
        i++;
       if (t.p[i]==t.p[i-1])
        error(7302);
       randtable_result=t.x[i-1]+(r-t.p[i-1])/(t.p[i]-t.p[i-1])*(t.x[i]-t.x[i-1]);
     }
     return randtable_result;
  }

void inlt(plistt& lt,ptransact t)
  {
    t->translist=lt;
    {
      listt& with = *lt;

      if (with.first==nil)
       {
         with.first=t;
         t->sled=t;
         t->pred=t;
       } else
       {
         t->sled=with.first;
         t->pred=with.first->pred;
         with.first->pred->sled=t;
         with.first->pred=t;
         with.first=t;
       }
      {
         parml& with1 = with.p;

         with1.ll=with1.ll+1;
         if (with1.ll>with1.lm)
          with1.lm=with1.ll;
      }
    }
  }

void outtlist(plistt& lt)
  {
    ptransact t;

    { listt& with = *lt;
     if (with.first!=nil)
      {
        t=with.first;
        t->translist=nil;
        if (with.p.ll==1)
         with.first=nil; else
         {
           with.first=t->sled;
           t->pred->sled=t->sled;
           t->sled->pred=t->pred;
         }
        t->sled=t;
        t->pred=t;
        with.p.ll=with.p.ll-1;
      } else
      error(701);}
  }

void inlf(plistf& lf,pfacility f)
  {
    {
       listf& with = *lf;

       if (with.first!=nil)
        {
          f->sled=with.first;
          f->pred=with.first->pred;
          with.first->pred->sled=f;
          with.first->pred=f;
        }
       {
          parml& with1 = with.p;

          with1.ll=with1.ll+1;
          if (with1.ll>with1.lm)
           with1.lm=with1.ll;
       }
       with.first=f;
    }
  }

void inlq(plistq& lq,pqueue q)
  {
    {
       listq& with = *lq;

       if (with.first!=nil)
        {
          q->sled=with.first;
          q->pred=with.first->pred;
          with.first->pred->sled=q;
          with.first->pred=q;
        }
       {
          parml& with1 = with.p;

          with1.ll=with1.ll+1;
          if (with1.ll>with1.lm)
           with1.lm=with1.ll;
       }
       with.first=q;
    }
  }

void inls(plists& ls,pstorage st)
  {
    {
       lists& with = *ls;

       if (with.first!=nil)
        {
          st->sled=with.first;
          st->pred=with.first->pred;
          with.first->pred->sled=st;
          with.first->pred=st;
        }
       {
          parml& with1 = with.p;

          with1.ll=with1.ll+1;
          if (with1.ll>with1.lm)  with1.lm=with1.ll;
       }
       with.first=st;
    }
  }

void inlh(plisth& lh,phistogram h)
  {
    {
       listh& with = *lh;

       if (with.first!=nil)
        {
          h->sled=with.first;
          h->pred=with.first->pred;
          with.first->pred->sled=h;
          with.first->pred=h;
        }
       {
          parml& with1 = with.p;

          with1.ll=with1.ll+1;
          if (with1.ll>with1.lm)
           with1.lm=with1.ll;
       }
       with.first=h;
    }
  }

void outflist(plistf& lf)
  {
    pfacility f;

    { listf& with = *lf;
     if (with.first!=nil)
      {
        f=with.first;
        if (with.p.ll==1)
         with.first=nil; else
         {
           with.first=f->sled;
           f->pred->sled=f->sled;
           f->sled->pred=f->pred;
         }
        f->sled=f;
        f->pred=f;
        with.p.ll=with.p.ll-1;
      } else
      error(701);}
  }

void outqlist(plistq& lq)
  {
    pqueue q;

    { listq& with = *lq;
     if (with.first!=nil)
      {
        q=with.first;
        if (with.p.ll==1)
         with.first=nil; else
         {
           with.first=q->sled;
           q->pred->sled=q->sled;
           q->sled->pred=q->pred;
         }
        q->sled=q;
        q->pred=q;
        with.p.ll=with.p.ll-1;
      } else
      error(701);}
  }
void outslist(plists ls)
  {
    pstorage st;

    { lists& with = *ls;
     if (with.first!=nil)
      {
        st=with.first;
        if (with.p.ll==1)
         with.first=nil; else
         {
           with.first=st->sled;
           st->pred->sled=st->sled;
           st->sled->pred=st->pred;
         }
        st->sled=st;
        st->pred=st;
        with.p.ll=with.p.ll-1;
      } else
      error(701);}
  }
void outhlist(plisth lh)
  {
    phistogram h;

    { listh& with = *lh;
     if (with.first!=nil)
      {
        h=with.first;
        if (with.p.ll==1)
         with.first=nil; else
         {
           with.first=h->sled;
           h->pred->sled=h->sled;
           h->sled->pred=h->pred;
         }
        h->sled=h;
        h->pred=h;
        with.p.ll=with.p.ll-1;
      } else
      error(701);}
  }

 void indelist(ptransact& t)
   {
     int i;

     {
        transact& with = *t;

        for( i=1; i <= mptb; i ++)
           with.pb[i]=false;
        for( i=1; i <= mptf; i ++)
           with.pf[i]=nil;
        for( i=1; i <= mptq; i ++)
           with.pq[i]=nil;
        for( i=1; i <= mpts; i ++)
           with.ps[i]=nil;
        for( i=1; i <= mpti; i ++)
           with.pi[i]=0;
        for( i=1; i <= mptr; i ++)
           with.pr[i]=0.0;
        with.eve=0;
        with.nexttime=0;
        with.nans=1;
        inlt(delist,t);
        with.predans=t;
        with.sledans=t;
        with.prty=0;
        with.ans=with.nom;
        with.testprty=false;
     }
   }

void infuture(ptransact& t)
  {
/*    outfile<<">>> BEFORE <<<"<<endl;
    prnlt(future);
    outfile<<">>> <<<"<<endl; */

    ptransact t1;
    prtyrange pt;
    real nt;

    pt=t->prty;
    nt=t->nexttime;
    { listt& with = *future;
     if (with.first==nil)
      inlt(future,t); else
      if ((with.first->nexttime>nt) || ((with.first->nexttime==nt)
         && (pt>with.first->prty)))
       inlt(future,t); else
       {
         t1=with.first;
         while ((nt<with.first->pred->nexttime) || ((nt==with.first->pred->nexttime)
               && (pt>with.first->pred->prty)))
          with.first=with.first->pred;
         inlt(future,t);
         with.first=t1;
       }}
    t->testprty=true;

/*    outfile<<">>> AFTER <<<"<<endl;
    prnlt(future);
    outfile<<">>> <<<"<<endl; */
  }

void incurrent(ptransact& t)
  {
    ptransact t1;
    prtyrange pt;

    { listt& with = *current;
     if (with.first==nil)
      inlt(current,t); else
      if (t->prty>with.first->prty)
       {
         inlt(current,t);
         if (trans!=nil)
          {
            trans->eve=succ(event,sysevent);
            trans=nil;
          }
       } else
       {
         t1=with.first;
         pt=t->prty;
         while ((pt>with.first->pred->prty)==true)
          with.first=with.first->pred;
         inlt(current,t);
         with.first=t1;
       }}
    t->testprty=true;
  }

void inlfifo(plistt lt)
  {
    if (trans==nil)
     error(702); else
     {
       outtlist(current);
       inlt(lt,trans);
       trans->testprty=false;
       lt->first=lt->first->sled;
       trans=nil;
     }
  }

void inllifo(plistt lt)
  {
    if (trans==nil)
     error(702); else
     {
       trans->testprty=false;
       outtlist(current);
       inlt(lt,trans);
       trans=nil;
     }
  }

void outuserlt(plistt lt)
  {
    ptransact t;

    t=lt->first;
    outtlist(lt);
    incurrent(t);
    t->eve=succ(event,t->eve);
  }

void initcreate(event e,real r)
  {
    ptransact t;

    delist->first->nexttime=r;
    delist->first->eve=e;
    t=delist->first;
    outtlist(delist);
    infuture(t);
    if (trace)
     {
       tracerec.t=t;
       tracer(1);
     }
  }

void create(real r)
  {
    ptransact t;

    if (r<0)
     error(101);
    if (delist->first==nil)
     error(102);
    if (r!=0)
     {
       t=delist->first;
       t->nexttime=systime+r;
       t->eve=sysevent;
       outtlist(delist);
       infuture(t);
       if (trace)
        {
          tracerec.t=t;
          tracer(2);
        }
     }
  }

void destroy()
  {
    if (trans!=nil)
     {
       outtlist(current);
       indelist(trans);
       if (trace)
        tracer(3);
       trans=nil;
     } else
     error(201);
  }

void delayt(real r)
  {
    if (r<0)
     error(501);
    if (trans==nil)
     error(502);
    trans->nexttime=systime+r;
    trans->eve=succ(event,sysevent);
    if (trace)
    {
      tracerec.r=r;
      tracer(4);
    }
    outtlist(current);
    infuture(trans);
    trans=nil;
  }

void newtlist(plistt& l)
  {
    l = new listt;
    l->first=nil;
    {
       parml& with = l->p;

       with.timel=0;
       with.pretime=systime;
       with.ci=0;
       with.co=0;
       with.ll=0;
       with.lm=0;
    }
    l->sled=l;
    l->pred=l;
  }

void inwaitl(ptransact& t,event e)
  {
    ptransact t1;
    prtyrange pt;

    pt=t->prty;
    {
       listt& with = *waitl[e];

       if (with.first==nil)
        inlt(waitl[e],t); else
        if (with.first->prty<pt)
         inlt(waitl[e],t); else
         {
           t1=with.first;
           while (pt>with.first->pred->prty)
            with.first=with.first->pred;
           inlt(waitl[e],t);
           with.first=t1;
         }
       if (trace)
        {
          tracerec.e=e;
          tracer(5);
        }
    }
  }

void wait(event e)
  {
    if (trans==nil)
     error(502); else
     if (waitl[e]==nil)
      {
        newtlist(waitl[e]);
        waitl[e]->p.name="WAITL   ";
      }
    if (waitevent[e]==false)
     {
       outtlist(current);
       inwaitl(trans,e);
       trans->eve=succ(event,sysevent);
       trans=nil;
     } else
     waitevent[e]=false;
  }

void next(event e)
  {
    if (trans==nil)
     error(802);
    if (e<1)
     error(801);
    trans->eve=e;
    if (trace)
     {
       tracerec.e=e;
       tracer(6);
     }
    trans=nil;
  }

void infac(pfacility& f)
  {
    plistt lt;
    ptransact t;

    if (trans==nil)
     error(403); else
     { facility& with = *f;
      if (with.test)
       {
         if (with.status!=with.free)
          if (with.transpoint->translist==current)
           {
             if (waitl[with.transpoint->eve]==nil)
              {
                newtlist(waitl[with.transpoint->eve]);
                waitl[with.transpoint->eve]->p.name=" WAITL  ";
              }
             outtlist(current);
             inwaitl(trans,with.transpoint->eve);
             if (trace)
              {
                tracerec.f=f;
                tracer(7);
              }
             trans=nil;
           } else
           {
             if (trace)
              {
                tracerec.f=f;
                tracer(8);
              }
             with.p=with.p+1;
             with.status=with.preempted;
             with.ci=with.ci+1;
             if (with.inter==nil)
              {
                newtlist(with.inter);
                with.inter->p.name=with.name;
                /*with.inter->p.name[7]=' ';
                with.inter->p.name[8]='I';*/
              }
             lt=with.transpoint->translist;
             t=lt->first;
             with.transpoint->nexttime=with.transpoint->nexttime-systime;
             while (lt->first!=with.transpoint)
              lt->first=lt->first->sled;
             outtlist(lt);
             if (with.transpoint!=t)
              lt->first=t;
             inlt(with.inter,with.transpoint);
             with.transpoint->translist=lt;
             with.transpoint->testprty=false;
             with.transpoint=trans;
           } else
          {
            with.status=with.seized;
            with.pretime=systime;
            with.transpoint=trans;
            with.ci=with.ci+1;
            if (trace)
             {
               tracerec.f=f;
               tracer(9);
             }
          }
       }}
  }
void outfac(pfacility& f)
  {
    ptransact t;
    plistt lt;

    if (f->test)
     {
        facility& with = *f;

        if (trans==nil)
         error(404);
        if (with.transpoint==nil)
         error(402);
        if (with.transpoint!=trans)
         error(405);
        if (trace)
         {
           tracerec.f=f;
           tracer(10);
         }
        if (with.inter==nil)
         {
           with.transpoint=nil;
           with.status=with.free;
           with.timef=with.timef+systime-with.pretime;
           if (with.fl->first!=nil)
            {
              t=with.fl->first;
              outtlist(with.fl);
              incurrent(t);
            }
         } else
         if (with.inter->first!=nil)
          {
            with.transpoint=with.inter->first;
            lt=with.transpoint->translist;
            outtlist(with.inter);
            if (with.inter->first==nil)
            with.status=with.seized;
            if (trace)
             {
               tracerec.f=f;
               tracer(11);
             }
            if (lt==future)
             {
               with.transpoint->nexttime=systime+with.transpoint->nexttime;
               infuture(f->transpoint);
             } else
             inlt(lt,with.transpoint);
          } else
          {
            with.transpoint=nil;
            with.status=with.free;
            with.timef=with.timef+systime-with.pretime;
            if (with.fl->first!=nil)
             {
               t=with.fl->first;
               outtlist(with.fl);
               incurrent(t);
             }
          }
        if (with.ci!=0)
         with.mtime=with.timef/with.ci; else
         with.mtime=0.0;
        if (systime!=resettime)
         with.pro=with.timef/(systime-resettime); else
         with.pro=0.0;
     }
  }

void outqueue(pqueue& q)
  {
    if (q->test)
     { queue& with = *q;
      if (with.status==with.empty)
       error(302); else
       {
         with.timeq=with.timeq+with.lq*(systime-with.pretime);
         with.lq=with.lq-1;
         if (with.lq==0)
          with.status=with.empty;
         if (with.pretime==systime)
          with.co=with.co+1;
         with.pretime=systime;
         if (trace)
          {
            tracerec.q=q;
            tracer(12);
          }
         if (systime!=resettime)
          with.lm=with.timeq/(systime-resettime); else
          with.lm=with.lq;
         if (with.ci!=0)
          with.mtime=with.timeq/with.ci; else
          with.mtime=with.timeq;
       }}
  }

void inqueue(pqueue& q)
  {
    if (q->test)
     {
        queue& with = *q;

        if (with.size<=with.lq)
         error(301);
        with.timeq=with.timeq+with.lq*(systime-with.pretime);
        with.lq=with.lq+1;
        with.ci=with.ci+1;
        with.pretime=systime;
        if (with.lq>with.mq)
         with.mq=with.lq;
        with.status=with.full;
        if (trace)
         {
           tracerec.q=q;
           tracer(13);
         }
     }
  }

void seize(pfacility& f)
  {
    ptransact t;

    if (trans==nil)
     error(403);
    if (f->test)
     {
        facility& with = *f;

        if (with.status!=with.free)
         {
           if (trace)
            {
              tracerec.f=f;
              tracer(14);
            }
           outtlist(current);
           if (with.fl->first==nil)
            inlt(with.fl,trans); else
            if (with.fl->first->prty<trans->prty)
             inlt(with.fl,trans); else
             {
               t=with.fl->first;
               while (trans->prty>with.fl->first->pred->prty)
                with.fl->first=with.fl->first->pred;
               inlt(with.fl,trans);
               with.fl->first=t;
             }
           trans=nil;
         } else
         {
           with.status=with.seized;
           with.transpoint=trans;
           with.pretime=systime;
           with.ci=with.ci+1;
           if (trace)
            {
              tracerec.f=f;
              tracer(15);
            }
         }
     }
  }

void enter(pstorage st,int n)
  {
    ptransact t;

    if (st->test)
     {
        storage& with = *st;

        if (with.s<n)
         error(411);
        if (trans==nil)
         error(412);
        if (with.sf>=n)
         {
           with.times=with.times+with.ss*(systime-with.pretime);
           with.pretime=systime;
           with.ss=with.ss+n;
           with.ci=with.ci+n;
           with.sf=with.sf-n;
           if (with.ss>with.sm)
            with.sm=with.ss;
           if (trace)
            {
              tracerec.n=n;
              tracerec.s=st;
              tracer(16);
            }
         } else
         {
           if (trace)
            {
              tracerec.s=st;
              tracer(17);
            }
           outtlist(current);
           if (with.slt->first==nil)
            inlt(with.slt,trans); else
            if (with.slt->first->prty<trans->prty)
             inlt(with.slt,trans); else
             {
               t=with.slt->first;
               while (trans->prty>with.slt->first->pred->prty)
                with.slt->first=with.slt->first->pred;
               inlt(with.slt,trans);
               with.slt->first=t;
             }
             trans=nil;
         }
     }
  }

void leave(pstorage st,int n)
  {
    ptransact t;

    if (st->test)
     {
        storage& with = *st;

        if (n>with.s)
         error(413);
        if (n>with.ss)
         error(413);
        if (trace)
         {
           tracerec.n=n;
           tracerec.s=st;
           tracer(18);
         }
        with.times=with.times+with.ss*(systime-with.pretime);
        with.ss=with.ss-n;
        with.sf=with.sf+n;
        with.pretime=systime;
        if (systime!=resettime)
         {
           with.ut=with.times/((systime-resettime)*with.s);
           with.smean=with.times/(systime-resettime);
         } else
         {
           with.ut=0.0;
           with.smean=with.ss*1.0;
         }
        if (with.ci!=0)
         with.mtime=with.times/with.ci;
        if (with.slt->first!=nil)
         {
           t=with.slt->first;
           outtlist(with.slt);
           incurrent(t);
           if (trace)
            {
              tracerec.t=t;
              tracer(19);
            }
         }
     }
  }

void parmans(parmtype typ,int n)
  {
    ptransact t;
    int j;

    if (trans==nil)
     error(717);
    t=trans;
    if (trace)
     {
       tracer(20);
       switch (typ) {
        case parmb: tracer(201); break;
        case parmi: tracer(202); break;
        case parmr: tracer(203); break;
        case parmf: tracer(204); break;
        case parmq: tracer(205); break;
        case parms: tracer(206);
        break;
       }
      tracer(207);
       switch (typ) {
        case parmb: tracer(208); break;
        case parmi: tracer(209); break;
        case parmr: tracer(210); break;
        case parmf: tracer(211); break;
        case parmq: tracer(212); break;
        case parms: tracer(213);
        break;
       }
      tracer(214);
     }
    { transact& with = *trans;
    for( j=1; j <= with.nans; j ++)
     {
       if (trace)
        {
          tracerec.t=t;
          tracer(21);
        }
       switch (typ) {
        case parmb: t->pb[n]=with.pb[n]; break;
        case parmi: t->pi[n]=with.pi[n]; break;
        case parmr: t->pr[n]=with.pr[n]; break;
        case parmf: t->pf[n]=with.pf[n]; break;
        case parmq: t->pq[n]=with.pq[n]; break;
        case parms: t->ps[n]=with.ps[n];
        break;
       }
       t=t->sledans;
     }}
  }

void newslist(plists& ls)
  {
    ls = new lists;
    ls->pred=ls;
    ls->sled=ls;
    ls->first=nil;
    {
       parml& with = ls->p;

       with.timel=0;
       with.pretime=systime;
       with.ci=0;
       with.co=0;
       with.ll=0;
       with.lm=0;
    }
  }

void newflist(plistf& lf)
  {
    lf = new listf;
    lf->first=nil;
    lf->sled=lf;
    lf->pred=lf;
    {
       parml& with = lf->p;

       with.timel=0;
       with.pretime=systime;
       with.ci=0;
       with.co=0;
       with.ll=0;
       with.lm=0;
    }
  }

void newqlist(plistq& lq)
  {
    lq = new listq;
    lq->first=nil;
    lq->sled=lq;
    lq->pred=lq;
    {
       parml& with = lq->p;

       with.timel=0;
       with.pretime=systime;
       with.ci=0;
       with.co=0;
       with.ll=0;
       with.lm=0;
    }
  }

void newhist(phistogram& hist,real min,real max,hint2 ih,
                  bool gr,alfa title)
  {
    unsigned char i;

    hist = new histogram;
    {
       histogram& with = *hist;

       with.total=0;
       with.sum=0.0;
       with.sumsqr=0.0;
       with.maxx=max;
       with.minx=min;
       with.ihint=ih;
       for( i=0; i <= with.ihint; i ++)
        with.x[i]=0;
       with.graf=gr;
       with.sled=hist;
       with.pred=hist;
       with.name=title;
       inlh(histlist,hist);
    }
    histlist->first=histlist->first->sled;
  }

void destrh(phistogram& hist)
  {
    { listh& with = *histlist;
     while (with.first!=hist)
      with.first=with.first->sled;}
    outhlist(histlist);
    delete hist;
  }

void newqueue(pqueue& q,alfa nameq)
  {
    q = new queue;
    {
       queue& with = *q;

       with.status=with.empty;
       with.lq=0;
       with.mq=0;
       with.size=itransmax;
       with.mtime=0;
       with.co=0;
       with.ci=0;
       with.timeq=0;
       with.pretime=systime;
       with.name=nameq;
       with.sled=q;
       with.pred=q;
       inlq(quelist,q);
       with.test=true;
       quelist->first=quelist->first->sled;
    }
  }
void newfac(pfacility& f,alfa namef)
  {
    f = new facility;
    {
       facility& with = *f;

       with.status=with.free;
       with.transpoint=nil;
       with.sled=f;
       with.pred=f;
       with.timef=0;
       with.ci=0;
       with.pretime=systime;
       newtlist(with.fl);
       with.name=namef;
       with.p=0;
       with.inter=nil;
       inlf(faclist,f);
       with.fl->p.name=namef;
       faclist->first=faclist->first->sled;
       with.test=true;
    }
  }

void newstorage(pstorage& st,alfa names,int s1)
  {
    st = new storage;
    {
       storage& with = *st;

       newtlist(with.slt);
       with.s=s1;
       with.name=names;
       with.smean=0;
       with.ss=0;
       with.sf=s1;
       with.sm=0;
       with.times=0;
       with.ci=0;
       with.pretime=systime;
       with.mtime=0.0;
       with.sled=st;
       with.pred=st;
       inls(stlist,st);
       with.test=true;
    }
    stlist->first=stlist->first->sled;
  }

void newuserlt(plistt& lt,alfa name)
  {
    newtlist(lt);
    lt->p.name=name;
     {
       userlist.ll=userlist.ll+1;
       if (userlist.first==nil)
        userlist.first=lt; else
        {
          lt->sled=userlist.first;
          lt->pred=userlist.first->pred;
          userlist.first->pred->sled=lt;
          userlist.first->pred=lt;
          userlist.first=lt;
        }
     }
  }

void destrs(pstorage& st)
  {
    if (st==nil)
     error(204);
    if (st->slt->first!=nil)
     error(208);
    if (st->ss!=0)
     error(209);
    delete st->slt;
    { lists& with = *stlist;
     while (with.first!=st)
      with.first=with.first->sled;}
    outslist(stlist);
    delete st;
    st=nil;
  }

void destrf(pfacility& f)
  {
    if (f==nil)
     error(202); else
     {
        facility& with = *f;

        if (with.status==with.seized)
         error(205);
        if (with.fl->first!=nil)
         error(206);
        if (with.inter!=nil)
         {
           if (with.inter->first!=nil)
            error(207);
           delete with.inter;
         }
     }
     { listf& with = *faclist;
      while (with.first!=f)
       with.first=with.first->sled;}
     outflist(faclist);
     delete f->fl;
     delete f;
     f=nil;
  }
void destrq(pqueue& q)
  {
    if (q==nil)
     error(203); else
     {
       { listq& with = *quelist;
        while (with.first!=q)
         with.first=with.first->sled;}
       outqlist(quelist);
       delete q;
       q=nil;
     }
  }

void newhlist(plisth& lh)
  {
    lh = new listh;
    {
       listh& with = *lh;

       with.first=nil;
       with.sled=lh;
       with.pred=lh;
       {
          parml& with1 = with.p;

          with1.timel=0;
          with1.pretime=systime;
          with1.ci=0;
          with1.co=0;
          with1.ll=0;
          with1.lm=0;
       }
    }
  }
void destrlt(plistt& lt)
  {
    ptransact t;

    if (lt==nil)
     error(211); else
     {
        {
          while (lt!=userlist.first)
           userlist.first=userlist.first->sled;
          userlist.ll=userlist.ll-1;
          if (userlist.ll==0)
           userlist.first=nil; else
           {
             {
                listt& with1 = *userlist.first;

                with1.sled->pred=with1.pred;
                with1.pred->sled=with1.sled;
             }
             userlist.first=lt->sled;
           }
        }
       { listt& with = *lt;
        if (with.p.ll!=0)
         {
           error(210);
           while (with.p.ll!=0)
            {
              t=with.first;
              outtlist(lt);
              indelist(t);
            }
         }}
       delete lt;
     }
  }

void split(int n,event e)
  {
    int i,
    j;
    ptransact t1,
    t;

    if (trans==nil)
     error(711);
    if (n<1)
     error(713);
    if (delist->p.ll<n)
     error(716);
    t1=trans;
    trans->nans=trans->nans+n;
    if (trace)
     {
       tracerec.n=n;
       tracerec.e=e;
       tracer(22);
     }
    { transact& with = *trans;
     for( i=1; i <= n; i ++)
      {
        t=delist->first;
        outtlist(delist);
        t->eve=e;
        t->predans=t1;
        t1->sledans=t;
        t->ans=with.ans;
        t->nexttime=with.nexttime;
        t->prty=with.prty;
        t->nans=with.nans;
        for( j=1; j <= 2; j ++)
         {
           t->pb[j]=with.pb[j];
           t->pf[j]=with.pf[j];
           t->pq[j]=with.pq[j];
           t->ps[j]=with.ps[j];
         }
        for( j=1; j <= 3; j ++)
         {
           t->pi[j]=with.pi[j];
           t->pr[j]=with.pr[j];
         }
        incurrent(t);
        t1=t;
      }}
  }
void assemble(int n)
  {
    ptransact t;
    int k,
    i;

    if (trans==nil)
     error(712);
    if (n<1)
     error(714);
    if (ass[sysevent]==nil)
     {
       newtlist(ass[sysevent]);
       ass[sysevent]->p.name="ASSEMBLE";
     }
    i=0;
    if (ass[sysevent]->first==nil)
     {
       outtlist(current);
       inlt(ass[sysevent],trans);
       trans->testprty=false;
       if (trace)
        tracer(23);
       trans->pi[1]=0;
       if (trans->nans<n)
        error(715);
     } else
     { listt& with = *ass[sysevent];
      while ((with.first->ans!=trans->ans) && (i<with.p.ll))
       {
         with.first=with.first->sled;
         i=i+1;
       }}
     if (ass[sysevent]->first->ans!=trans->ans)
      {
        outtlist(current);
        inlt(ass[sysevent],trans);
        trans->testprty=false;
        if (trace)
         tracer(23);
        trans->pi[1]=0;
        if (trans->nans<n)
         error(715);
      }
     if (ass[sysevent]->first->pi[1] < (n-1))
      {
        {
           listt& with = *ass[sysevent];

           if (trace)  tracer(24);
           t=trans;
           k=trans->nans;
           with.first->nans=k-1;
           for( i=1; i <= k; i ++)
           {
             t->nans=k-1;
             t=t->sledans;
           }
           if (with.first!=trans)
            {
              outtlist(current);
              indelist(trans);
            }
           trans->sledans->predans=trans->predans;
           trans->predans->sledans=trans->sledans;
           trans=nil;
           with.first->pi[1]=with.first->pi[1]+1;
        }
      } else
      {
        t=ass[sysevent]->first;
        outtlist(ass[sysevent]);
        indelist(t);
        if (trace)
         tracer(25);
      }
  }

void priority(prtyrange p)
  {
    ptransact t,
    tt;
    int i;

    t=trans;
    trans->prty=p;
    if (trace)  tracer(26);
     for( i=1; i <= trans->nans; i ++)
      {
        t->prty=p;
        if (trace)
         {
           tracerec.t=t;
           tracer(27);
         }
        { transact& with = *t;
         if (with.testprty)
          {
            while (((with.prty>with.pred->prty) && (with.translist!=future) &&
                   (t!=with.translist->first)) || ((with.translist==future) &&
                   (with.nexttime==with.pred->nexttime) && (with.prty>with.pred->prty)&&
                   (t!=future->first)))
             {
               tt=with.pred;
               with.pred=tt->pred;
               tt->pred=t;
               tt->sled=with.sled;
               with.pred->sled=t;
               tt->sled->pred=tt;
               with.sled=tt;
               if (tt==with.translist->first)
                with.translist->first=t;
             }
            while (((with.prty<with.sled->prty) && (with.translist!=future) &&
                   (with.sled!=with.translist->first)) || ((with.translist==future) &&
                   (with.nexttime==with.sled->nexttime) && (with.prty<with.sled->prty) &&
                   (with.sled!=future->first)))
             {
               tt=t->sled;
               with.sled=tt->sled;
               tt->sled=t;
               tt->pred=with.pred;
               with.sled->pred=t;
               tt->pred->sled=tt;
               with.pred=tt;
             }
          }}
         t=t->sledans;
      }
  }

void tabulate(phistogram hist,real t)
  {
    int ind;

    {
       histogram& with = *hist;

       with.total=with.total+1;
       with.sum=with.sum+t;
       with.sumsqr=with.sumsqr+t*t;
       if (t < with.minx)
        with.x[0]=with.x[0]+1; else
        if (t >= with.maxx)
         with.x[with.ihint]=with.x[with.ihint]+1; else
         {
           ind=trunc((t-with.minx)/(with.maxx-with.minx)*(with.ihint-1))+1;
           with.x[ind]= with.x[ind]+1;
         }
    }
  }

void accept(unsigned char sg)
  {
    ptransact t;
    prtyrange pt;

    if (trans==nil)
     error(512); else
     {
       pt=trans->prty;
       trans->eve=succ(event,sysevent);
       if (signlist[sg]==nil)
        {
          newtlist(signlist[sg]);
          signlist[sg]->p.name="SG      ";
        }
       outtlist(current);
       if (trace)
        {
          tracerec.n=sg;
          tracer(28);
        }
       { listt& with = *signlist[sg];
        if (with.first==nil)
         inlt(signlist[sg],trans); else
         if (with.first->prty<pt)
          inlt(signlist[sg],trans); else
          {
            t=with.first;
            while (pt>with.first->pred->prty)
             with.first=with.first->pred;
            inlt(signlist[sg],trans);
            with.first=t;
          }}
       trans=nil;
     }
  }
  
void send(unsigned char sg)
  {
    int i,n;
    ptransact t;

    if (signlist[sg]==nil)
     error(512); else
     { listt& with = *signlist[sg];
      if (with.first!=nil)
       {
         n=with.p.ll;
         for( i=1; i <= n; i ++)
          {
            t=with.first;
            outtlist(signlist[sg]);
            incurrent(t);
          }
         if (trace)
          {
            tracerec.n=sg;
            tracer(29);
          }
       } else
       if (trace)
        {
          tracerec.n=sg;
          tracer(30);
        }}
  }

void resetall();

static void resetp(parml& p)
  {
     {
       p.timel=0.0;
       p.pretime=systime;
       p.ci=0;
       p.co=0;
       p.lm=p.ll;
     }
  }

void resetall()
  {
    int i,
    j;

    resetp(delist->p);
    resetp(current->p);
    resetp(future->p);
    resettime=systime;
    {
       listf& with = *faclist;

       for( i=1; i <= with.p.ll; i ++)
        {
          {
             facility& with1 = *with.first;

             with1.ci=0;
             with1.timef=0.0;
             with1.mtime=0.0;
             with1.pro=0.0;
             with1.pretime=systime;
             with1.p=0;
             resetp(with1.fl->p);
             if (with1.inter!=nil)
              resetp(with1.inter->p);
          }
          with.first=with.first->sled;
        }
       resetp(with.p);
    }
    {
       listh& with = *histlist;

       for( i=1; i <= with.p.ll; i ++)
        {
          {
             histogram& with1 = *with.first;

             with1.total=0;
             with1.sum=0.0;
             with1.sumsqr=0.0;
             for( j=0; j <= with1.ihint; j ++)
              with1.x[j]=0;
          }
          with.first=with.first->sled;
        }
       resetp(with.p);
    }
    {
       lists& with = *stlist;

       for( i=1; i <= with.p.ll; i ++)
        {
          {
             storage& with1 = *with.first;

             with1.ci=0;
             with1.times=0.0;
             with1.mtime=0.0;
             with1.ut=0.0;
             with1.sm=with1.ss;
             with1.smean=0.0;
             with1.pretime=systime;
             resetp(with1.slt->p);
          }
          with.first=with.first->sled;
        }
       resetp(with.p);
    }
     for( i=1; i <= userlist.ll; i ++)
      {
        resetp(userlist.first->p);
        userlist.first=userlist.first->sled;
      }
    {
       listq& with = *quelist;

       for( i=1; i <= with.p.ll; i ++)
        {
         {
            queue& with1 = *with.first;

            with1.mq=with1.lq;
            with1.co=0;
            with1.ci=0;
            with1.timeq=0.0;
            with1.mtime=0.0;
            with1.pretime=systime;
         }
         with.first=with.first->sled;
       }
      resetp(with.p);
    }
   for( i=1; i <= evemax; i ++)
    {
      if (waitl[i]!=nil)
       resetp(waitl[i]->p);
      maxevent[i]=0;
    }
  }

void clear();

static void clearlist(plistt lt)
  {
    ptransact t;

    { listt& with = *lt;
     while (with.p.ll!=0)
      {
        t=with.first;
        outtlist(lt);
        indelist(t);
      }}
  }

void clear()
  {
    int i;

    clearlist(future);
    clearlist(current);
    for( i=1; i <= signmax; i ++)
     if (signlist[i]!=nil)
      clearlist(signlist[i]);
    for( i=1; i <= evemax; i ++)
     {
       if (waitl[i]!=nil)
        clearlist(waitl[i]);
       waitevent[i]=false;
       if (ass[i]!=nil)
        clearlist(ass[i]);
     }
    { listf& with = *faclist;
     for( i=1; i <= with.p.ll; i ++)
      {
        {
           facility& with1 = *with.first;

           with1.status=with1.free;
           with1.transpoint=nil;
           clearlist(with1.fl);
           if (with1.inter!=nil)
            if (with1.inter->first!=nil)
             clearlist(with1.inter);
        }
        with.first=with.first->sled;
      }}
    { listq& with = *quelist;
     for( i=1; i <= with.p.ll; i ++)
      {
        {
           queue& with1 = *with.first;

           with1.status=with1.empty;
           with1.lq=0;
        }
        with.first=with.first->sled;
      }}
    { lists& with = *stlist;
     for( i=1; i <= with.p.ll; i ++)
      {
        {
           storage& with1 = *with.first;

           with1.ss=0;
           with1.sf=with1.s;
           clearlist(with1.slt);
        }
        with.first=with.first->sled;
      }}
     for( i=1; i <= userlist.ll; i ++)
      {
        clearlist(userlist.first);
        userlist.first=userlist.first->sled;
      }
    resetall();
    systime=0.0;
    resettime=0.0;
    trans=nil;
  }
void initlist(int itr)
  {
    ptransact pl;
    int i;
    cstring<255> file_name;
    char ch;

    systime=0.0;
    resettime=0.0;
    sysevent=1;
    trans=nil;
    newtlist(delist);
    newtlist(future);
    newqlist(quelist);
    newtlist(current);
    newflist(faclist);
    newslist(stlist);
    newhlist(histlist);
    current->p.name="CURRENT ";
    future->p.name="FUTURE  ";
    delist->p.name="DELIST  ";
    for( i=1; i <= evemax; i ++)
     {
       waitl[i]=nil;
       ass[i]=nil;
       waitevent[i]=false;
       maxevent[i]=0;
     }
    itransmax=itr;
    eventall=0;
    for( i=itransmax; i >= 1; i --)
     {
       pl = new transact;
       pl->nom=i;
       indelist(pl);
     }
/*    ClrScr;*/
/*    output << " Using dialog (Y - yes / any key - not) ?";
    input >> ch; */
    ch = 'N';
    if ((ch=='Y')||(ch=='y'))
     {
       dialogus=true;
       outfile.open("TTY");
       //getcurdir(0,str2.asarray_new());
       output << " Directorie with packed menus (PIC*.PAC) --> ";
       //input >> str1/* >> NL */;
     } else
     {
       dialogus=false;
       output << " Enter input file name  --> ";
       input >> file_name/* >> NL */;
       const char* ext= ".html";
       strcat(file_name.asarray_new(),ext);
       outfile.open(file_name.asarray_new(),ios::out);
     }
    outfile.setf(ios::fixed);
    prnhead();
    errtest=false;
     {
       diarec.test=true;
       diarec.errinput=false;
       diarec.endtest=false;
       diarec.stoptest=false;
     }
    userlist.first=nil;
    trace=false;
    userlist.ll=0;
    ctime1=0.0;
    ctime2=0.0;
    realtime=0.0;
    v0=17;  v1=1;  v2=2;   v3=3;  v4=4;   v5=5;   v6=6;   v7=7;
    v8=8;  v9=9; v10=10; v11=11; v12=12; v13=13; v14=14; v15=15;
  }

void plan()
  {
    ptransact t;

    ctime2=_clock();
    if (ctime1!=0.0)
     realtime=realtime+ctime2-ctime1;
    ctime1=ctime2;
    if (waitl[sysevent]!=nil)
     if (waitl[sysevent]->first!=nil)
      {
        t=waitl[sysevent]->first;
        outtlist(waitl[sysevent]);
        incurrent(t);
      } else
      waitevent[sysevent]=true;
    if (trans==nil)
     {
       if (current->first!=nil)
        trans=current->first; else
        {
           listt& with = *future;

           if (with.first!=nil)
            {
              systime=with.first->nexttime;
              trans=with.first;
              outtlist(future);
              incurrent(trans);
              if (trace)  tracer(0);
            } else
            error(602);
           if (with.first!=nil)
            if (with.first->nexttime==systime)
             if (with.first->pred->nexttime==systime)
              while (with.p.ll>0)
               {
                 t=with.first;
                 outtlist(future);
                 incurrent(t);
               } else
               while (with.first->nexttime==systime)
                {
                  t=with.first;
                  outtlist(future);
                  incurrent(t);
                }
        }
        sysevent=trans->eve;
     } else
     {
       sysevent=succ(event,sysevent);
       trans->eve=sysevent;
     }
    maxevent[sysevent]=maxevent[sysevent]+1;
    eventall=eventall+1;
  }
