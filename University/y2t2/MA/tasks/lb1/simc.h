#pragma warning(disable : 4996)

#ifndef SIMC_H
#define SIMC_H

#include <cstdio>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstring>

using namespace std;

template <int min, int max, typename t>
class array_new
{
  t mem[max + 1 - min];

public:
  array_new() {}
  array_new(t *other);
  t &operator[](int index) { return mem[index - min]; }
  // friend ostream& operator<<(ostream& os,array_new<min,max,char> a);
};

template <int size>
class cstring
{
  char str[size + 1];

public:
  cstring();
  char *asarray_new(void);
};

// Êîíñòàíòû è ñòðóêòóðû
const int evemax = 1024;
const int signmax = 64;
const int hint = 33;
/*ÒðÀÍÇÀÊòÍÎ-ÎðÈÅÍòÈðÎÂÀÍÍûÅ ÊÎÍñòÀÍòû*/
const int prtymax = 10;
const int mptb = 2;
const int mptr = 3;
const int mpti = 3;
const int mptf = 2;
const int mptq = 2;
const int mpts = 2;
/*double=double;*/
typedef signed char prtyrange;
const int min_prtyrange = -prtymax;
const int max_prtyrange = prtymax;
typedef string alfa;
typedef unsigned short event;
const int min_event = 0;
const int max_event = evemax;
typedef unsigned char signalp;
const int min_signal = 1;
const int max_signal = signmax;
typedef unsigned char hint2;
const int min_hint2 = 2;
const int max_hint2 = hint;
typedef array_new<0, hint, int> harr;
enum parmtype
{
  parmb,
  parmi,
  parmr,
  parmf,
  parmq,
  parms,
  last_parmtype
};
typedef struct transact *ptransact;
typedef struct facility *pfacility;
typedef struct queue *pqueue;
typedef struct histogram *phistogram;
typedef struct storage *pstorage;
typedef struct listt *plistt;
typedef struct listf *plistf;
typedef struct listq *plistq;
typedef struct lists *plists;
typedef struct listl *plistl;
typedef struct listh *plisth;

struct facility
{
  enum
  {
    free,
    seized,
    preempted
  } status;
  pfacility sled, pred;
  ptransact transpoint;
  int p, ci;
  alfa name;
  double timef, pretime, mtime, pro;
  plistt fl, inter;
  bool test;
};

struct storage
{
  int s, ss, sf, sm, ci;
  double ut, smean, mtime, times, pretime;
  alfa name;
  pstorage pred, sled;
  plistt slt;
  bool test;
};

struct queue
{
  enum
  {
    empty,
    full
  } status;
  int lq, mq, size, ci, co;
  pqueue sled, pred;
  alfa name;
  double timeq, pretime, lm, mtime;
  bool test;
};

struct transact
{
  array_new<1, mptb, bool> pb;
  array_new<1, mpti, int> pi;
  array_new<1, mptr, double> pr;
  array_new<1, mptf, pfacility> pf;
  array_new<1, mptq, pqueue> pq;
  array_new<1, mpts, pstorage> ps;
  int nans, nom, ans;
  ptransact predans, sledans, pred, sled;
  event eve;
  prtyrange prty;
  double nexttime;
  plistt translist;
  bool testprty;
};

struct listl
{
  plistt first;
  int ll;
};

struct parml
{
  double timel, pretime;
  int ci, co, ll, lm;
  alfa name;
};

struct lists
{
  pstorage first;
  parml p;
  plists sled, pred;
};

struct listt
{
  ptransact first;
  parml p;
  plistt sled, pred;
};

struct listq
{
  pqueue first;
  parml p;
  plistq sled,
      pred;
};

struct listh
{
  phistogram first;
  parml p;
  plisth sled, pred;
};

struct listf
{
  pfacility first;
  parml p;
  plistf sled, pred;
};

struct histogram
{
  bool graf;
  alfa name;
  unsigned total;
  hint2 ihint;
  double sum, sumsqr, maxx, minx;
  phistogram sled, pred;
  harr x;
};

struct table
{
  array_new<1, hint, double> x, p;
  hint2 ihint;
};

struct typtrace
{
  pfacility f;
  pqueue q;
  ptransact t;
  pstorage s;
  event e;
  double r;
  int n;
};
typedef array_new<1, 10, char> a10;

struct typdata
{
  a10 menu;
  int act, x, y;
};
enum typsel
{
  nch,
  mch,
  rch,
  last_typsel
};

struct typnmr
{
  int i, x, y;
  bool test;
};

struct typdiarec
{
  array_new<1, 10, typdata> data;
  a10 menubase, menubuf;
  bool stoptest, endtest, test, errinput;
  alfa name;
  typnmr n, m, r;
  int k, nom, number, actbase, actbuf, xbase, ybase;
  double endtime, time, stoptime, steptime;
  plistt lt;
  pqueue que;
  pfacility fac;
  pstorage st;
  phistogram hist;
};

extern bool trace, errtest;
extern typdiarec diarec;
extern double resettime, systime;
extern event ievemax, sysevent;
extern int itransmax;
extern array_new<1, evemax, bool> waitevent;
extern array_new<1, evemax, int> maxevent;
extern listl userlist;
extern ptransact trans;
extern plistt delist, current, future;
extern plistq quelist;
extern plistf faclist;
extern plists stlist;
extern plisth histlist;
extern array_new<min_signal, max_signal, plistt> signlist;
extern array_new<1, evemax, plistt> ass, waitl;
extern long int v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15;
extern typtrace tracerec;
extern ptransact translabel;
extern double eventall;
extern ofstream outfile;
extern ifstream f;
extern cstring<60> str1, str2;
extern double ctime1, ctime2, realtime;
extern double msystime, mrealtime, evespeed;
extern bool dialogus;

// Ïðîöåäóðû ìîäåëèðîâàíèÿ:
double _clock();
void prnlt1(plistt &);
void prnlt(plistt &);
void prnhist(phistogram);
void prnt1(ptransact);
void prnq(pqueue);
void prns(pstorage);
void prnf(pfacility);
void prwaitl(void);
void prnuserlt(void);
void lfprint(plistf);
void lsprint(plists);
void prnlq(plistq);
void prnls(plists);
void prnlf(plistf);
void prnlh(plisth);
void prnq1(pqueue);
void prnf1(pfacility);
void prns1(pstorage);
void prnh1(phistogram);
void printall(void);
void tracer(int);
void error(int);
void error1(int &);
void error(int);
double rand01(long int &);
double randexp(double, long int &);
double randab(double, double, long int &);
double randnorm(double, double, long int &);
int randpoisson(double, long int &);
double randdtable(table, long int &);
double randtable(table, long int &);
void inlt(plistt &, ptransact);
void outtlist(plistt &);
void inlf(plistf &, pfacility);
void inlq(plistq &, pqueue);
void inls(plists &, pstorage);
void inlh(plisth &, phistogram);
void outflist(plistf &);
void outqlist(plistq &);
void outslist(plists);
void outhlist(plisth);
void indelist(ptransact &);
void infuture(ptransact &);
void incurrent(ptransact &);
void inlfifo(plistt);
void inllifo(plistt);
void outuserlt(plistt);
void initcreate(event, double);
void create(double);
void destroy(void);
void delayt(double);
void newtlist(plistt &);
void inwaitl(ptransact &, event);
void wait(event);
void next(event);
void infac(pfacility &);
void outfac(pfacility &);
void outqueue(pqueue &);
void inqueue(pqueue &);
void seize(pfacility &);
void enter(pstorage, int);
void leave(pstorage, int);
void parmans(parmtype, int);
void newslist(plists &);
void newflist(plistf &);
void newqlist(plistq &);
void newhist(phistogram &, double, double, hint2, bool, alfa);
void destrh(phistogram &);
void newqueue(pqueue &, alfa);
void newfac(pfacility &, alfa);
void newstorage(pstorage &, alfa, int);
void newuserlt(plistt &, alfa);
void destrs(pstorage &);
void destrf(pfacility &);
void destrq(pqueue &);
void newhlist(plisth &);
void destrlt(plistt &);
void split(int, event);
void assemble(int);
void priority(prtyrange);
void tabulate(phistogram, double);
void accept(signalp);
void send(signalp);
void resetall(void);
void clear(void);
void initlist(int);
void plan(void);
void closeoutput(void);
void waitchar(void);
void starttrace(void);

#endif // SIMC_H
