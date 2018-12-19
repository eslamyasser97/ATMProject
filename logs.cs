using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
namespace Info
{
    #region Logs
    public class Logs
    {
        #region Member Variables
        protected int _Num;
        protected int _ID;
        protected string _Date;
        protected int _Day;
        protected string _time;
        protected string _operation;
        protected int _st;
        protected int _totalwithdraw;
        protected int _totaldepposite;
        #endregion
        #region Constructors
        public Logs() { }
        public Logs(int ID, string Date, int Day, string time, string operation, int st, int totalwithdraw, int totaldepposite)
        {
            this._ID=ID;
            this._Date=Date;
            this._Day=Day;
            this._time=time;
            this._operation=operation;
            this._st=st;
            this._totalwithdraw=totalwithdraw;
            this._totaldepposite=totaldepposite;
        }
        #endregion
        #region Public Properties
        public virtual int Num
        {
            get {return _Num;}
            set {_Num=value;}
        }
        public virtual int ID
        {
            get {return _ID;}
            set {_ID=value;}
        }
        public virtual string Date
        {
            get {return _Date;}
            set {_Date=value;}
        }
        public virtual int Day
        {
            get {return _Day;}
            set {_Day=value;}
        }
        public virtual string Time
        {
            get {return _time;}
            set {_time=value;}
        }
        public virtual string Operation
        {
            get {return _operation;}
            set {_operation=value;}
        }
        public virtual int St
        {
            get {return _st;}
            set {_st=value;}
        }
        public virtual int Totalwithdraw
        {
            get {return _totalwithdraw;}
            set {_totalwithdraw=value;}
        }
        public virtual int Totaldepposite
        {
            get {return _totaldepposite;}
            set {_totaldepposite=value;}
        }
        #endregion
    }
    #endregion
}