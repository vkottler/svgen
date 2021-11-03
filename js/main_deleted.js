!(function (t, e) {
  typeof exports === "object" && typeof module === "object"
    ? (module.exports = e())
    : typeof define === "function" && define.amd
    ? define([], e)
    : typeof exports === "object"
    ? (exports.Redux = e())
    : (t.Redux = e());
})(this, function () {
  return (function (t) {
    function e(r) {
      if (n[r]) return n[r].exports;
      const o = (n[r] = { exports: {}, id: r, loaded: !1 });
      return t[r].call(o.exports, o, o.exports, e), (o.loaded = !0), o.exports;
    }
    var n = {};
    return (e.m = t), (e.c = n), (e.p = ""), e(0);
  })([
    function (t, e, n) {
      "use strict";
      function r(t) {
        return t && t.__esModule ? t : { default: t };
      }
      (e.__esModule = !0),
        (e.compose =
          e.applyMiddleware =
          e.bindActionCreators =
          e.combineReducers =
          e.createStore =
            void 0);
      const o = n(2);
      const i = r(o);
      const u = n(7);
      const c = r(u);
      const f = n(6);
      const a = r(f);
      const s = n(5);
      const d = r(s);
      const l = n(1);
      const p = r(l);
      const y = n(3);
      r(y);
      (e.createStore = i.default),
        (e.combineReducers = c.default),
        (e.bindActionCreators = a.default),
        (e.applyMiddleware = d.default),
        (e.compose = p.default);
    },
    function (t, e) {
      "use strict";
      function n() {
        for (var t = arguments.length, e = Array(t), n = 0; t > n; n++)
          e[n] = arguments[n];
        if (e.length === 0)
          return function (t) {
            return t;
          };
        const r = (function () {
          const t = e[e.length - 1];
          const n = e.slice(0, -1);
          return {
            v: function () {
              return n.reduceRight(function (t, e) {
                return e(t);
              }, t.apply(void 0, arguments));
            },
          };
        })();
        return typeof r === "object" ? r.v : void 0;
      }
      (e.__esModule = !0), (e.default = n);
    },
    function (t, e, n) {
      "use strict";
      function r(t) {
        return t && t.__esModule ? t : { default: t };
      }
      function o(t, e, n) {
        function r() {
          b === h && (b = h.slice());
        }
        function i() {
          return v;
        }
        function c(t) {
          if (typeof t !== "function")
            throw Error("Expected listener to be a function.");
          let e = !0;
          return (
            r(),
            b.push(t),
            function () {
              if (e) {
                (e = !1), r();
                const n = b.indexOf(t);
                b.splice(n, 1);
              }
            }
          );
        }
        function s(t) {
          if (!(0, u.default)(t))
            throw Error(
              "Actions must be plain objects. Use custom middleware for async actions."
            );
          if (void 0 === t.type)
            throw Error(
              'Actions may not have an undefined "type" property. Have you misspelled a constant?'
            );
          if (x) throw Error("Reducers may not dispatch actions.");
          try {
            (x = !0), (v = y(v, t));
          } finally {
            x = !1;
          }
          for (let e = (h = b), n = 0; e.length > n; n++) e[n]();
          return t;
        }
        function d(t) {
          if (typeof t !== "function")
            throw Error("Expected the nextReducer to be a function.");
          (y = t), s({ type: a.INIT });
        }
        function l() {
          let t;
          const e = c;
          return (
            (t = {
              subscribe: function (t) {
                function n() {
                  t.next && t.next(i());
                }
                if (typeof t !== "object")
                  throw new TypeError("Expected the observer to be an object.");
                n();
                const r = e(n);
                return { unsubscribe: r };
              },
            }),
            (t[f.default] = function () {
              return this;
            }),
            t
          );
        }
        let p;
        if (
          (typeof e === "function" && void 0 === n && ((n = e), (e = void 0)),
          void 0 !== n)
        ) {
          if (typeof n !== "function")
            throw Error("Expected the enhancer to be a function.");
          return n(o)(t, e);
        }
        if (typeof t !== "function")
          throw Error("Expected the reducer to be a function.");
        var y = t;
        var v = e;
        var h = [];
        var b = h;
        var x = !1;
        return (
          s({ type: a.INIT }),
          (p = { dispatch: s, subscribe: c, getState: i, replaceReducer: d }),
          (p[f.default] = l),
          p
        );
      }
      (e.__esModule = !0), (e.ActionTypes = void 0), (e.default = o);
      const i = n(4);
      var u = r(i);
      const c = n(11);
      var f = r(c);
      var a = (e.ActionTypes = { INIT: "@@redux/INIT" });
    },
    function (t, e) {
      "use strict";
      function n(t) {
        typeof console !== "undefined" &&
          typeof console.error === "function" &&
          console.error(t);
        try {
          throw Error(t);
        } catch (e) {}
      }
      (e.__esModule = !0), (e.default = n);
    },
    function (t, e, n) {
      function r(t) {
        if (!u(t) || l.call(t) != c || i(t)) return !1;
        const e = o(t);
        if (e === null) return !0;
        const n = s.call(e, "constructor") && e.constructor;
        return typeof n === "function" && n instanceof n && a.call(n) == d;
      }
      var o = n(8);
      var i = n(9);
      var u = n(10);
      var c = "[object Object]";
      const f = Object.prototype;
      var a = Function.prototype.toString;
      var s = f.hasOwnProperty;
      var d = a.call(Object);
      var l = f.toString;
      t.exports = r;
    },
    function (t, e, n) {
      "use strict";
      function r(t) {
        return t && t.__esModule ? t : { default: t };
      }
      function o() {
        for (var t = arguments.length, e = Array(t), n = 0; t > n; n++)
          e[n] = arguments[n];
        return function (t) {
          return function (n, r, o) {
            const u = t(n, r, o);
            let f = u.dispatch;
            let a = [];
            const s = {
              getState: u.getState,
              dispatch: function (t) {
                return f(t);
              },
            };
            return (
              (a = e.map(function (t) {
                return t(s);
              })),
              (f = c.default.apply(void 0, a)(u.dispatch)),
              i({}, u, { dispatch: f })
            );
          };
        };
      }
      e.__esModule = !0;
      var i =
        Object.assign ||
        function (t) {
          for (let e = 1; arguments.length > e; e++) {
            const n = arguments[e];
            for (const r in n)
              Object.prototype.hasOwnProperty.call(n, r) && (t[r] = n[r]);
          }
          return t;
        };
      e.default = o;
      const u = n(1);
      var c = r(u);
    },
    function (t, e) {
      "use strict";
      function n(t, e) {
        return function () {
          return e(t.apply(void 0, arguments));
        };
      }
      function r(t, e) {
        if (typeof t === "function") return n(t, e);
        if (typeof t !== "object" || t === null)
          throw Error(
            "bindActionCreators expected an object or a function, instead received " +
              (t === null ? "null" : typeof t) +
              '. Did you write "import ActionCreators from" instead of "import * as ActionCreators from"?'
          );
        for (var r = Object.keys(t), o = {}, i = 0; r.length > i; i++) {
          const u = r[i];
          const c = t[u];
          typeof c === "function" && (o[u] = n(c, e));
        }
        return o;
      }
      (e.__esModule = !0), (e.default = r);
    },
    function (t, e, n) {
      "use strict";
      function r(t) {
        return t && t.__esModule ? t : { default: t };
      }
      function o(t, e) {
        const n = e && e.type;
        const r = (n && '"' + n + '"') || "an action";
        return (
          "Given action " +
          r +
          ', reducer "' +
          t +
          '" returned undefined. To ignore an action, you must explicitly return the previous state.'
        );
      }
      function i(t) {
        Object.keys(t).forEach(function (e) {
          const n = t[e];
          const r = n(void 0, { type: c.ActionTypes.INIT });
          if (void 0 === r)
            throw Error(
              'Reducer "' +
                e +
                '" returned undefined during initialization. If the state passed to the reducer is undefined, you must explicitly return the initial state. The initial state may not be undefined.'
            );
          const o =
            "@@redux/PROBE_UNKNOWN_ACTION_" +
            Math.random().toString(36).substring(7).split("").join(".");
          if (void 0 === n(void 0, { type: o }))
            throw Error(
              'Reducer "' +
                e +
                '" returned undefined when probed with a random type. ' +
                ("Don't try to handle " +
                  c.ActionTypes.INIT +
                  ' or other actions in "redux/*" ') +
                "namespace. They are considered private. Instead, you must return the current state for any unknown actions, unless it is undefined, in which case you must return the initial state, regardless of the action type. The initial state may not be undefined."
            );
        });
      }
      function u(t) {
        for (var e = Object.keys(t), n = {}, r = 0; e.length > r; r++) {
          const u = e[r];
          typeof t[u] === "function" && (n[u] = t[u]);
        }
        let c;
        const f = Object.keys(n);
        try {
          i(n);
        } catch (a) {
          c = a;
        }
        return function () {
          const t =
            arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
          const e = arguments[1];
          if (c) throw c;
          for (var r = !1, i = {}, u = 0; f.length > u; u++) {
            const a = f[u];
            const s = n[a];
            const d = t[a];
            const l = s(d, e);
            if (void 0 === l) {
              const p = o(a, e);
              throw Error(p);
            }
            (i[a] = l), (r = r || l !== d);
          }
          return r ? i : t;
        };
      }
      (e.__esModule = !0), (e.default = u);
      var c = n(2);
      const f = n(4);
      const a = (r(f), n(3));
      r(a);
    },
    function (t, e) {
      function n(t) {
        return r(Object(t));
      }
      var r = Object.getPrototypeOf;
      t.exports = n;
    },
    function (t, e) {
      function n(t) {
        let e = !1;
        if (t != null && typeof t.toString !== "function")
          try {
            e = !!(t + "");
          } catch (n) {}
        return e;
      }
      t.exports = n;
    },
    function (t, e) {
      function n(t) {
        return !!t && typeof t === "object";
      }
      t.exports = n;
    },
    function (t, e, n) {
      (function (e) {
        "use strict";
        t.exports = n(12)(e || window || this);
      }.call(
        e,
        (function () {
          return this;
        })()
      ));
    },
    function (t, e) {
      "use strict";
      t.exports = function (t) {
        let e;
        const n = t.Symbol;
        return (
          typeof n === "function"
            ? n.observable
              ? (e = n.observable)
              : ((e =
                  typeof n.for === "function"
                    ? n.for("observable")
                    : n("observable")),
                (n.observable = e))
            : (e = "@@observable"),
          e
        );
      };
    },
  ]);
});

let f;
const aa = function (a) {
  let b = 0;
  return function () {
    return b < a.length ? { done: !1, value: a[b++] } : { done: !0 };
  };
};
const ba =
  typeof Object.defineProperties === "function"
    ? Object.defineProperty
    : function (a, b, c) {
        a != Array.prototype && a != Object.prototype && (a[b] = c.value);
      };
const p =
  typeof window !== "undefined" && window === this
    ? this
    : typeof global !== "undefined" && global != null
    ? global
    : this;
var u = function () {
  u = function () {};
  p.Symbol || (p.Symbol = ca);
};
var ca = (function () {
  let a = 0;
  return function (b) {
    return "jscomp_symbol_" + (b || "") + a++;
  };
})();
var v = function () {
  u();
  let a = p.Symbol.iterator;
  a || (a = p.Symbol.iterator = p.Symbol("iterator"));
  typeof Array.prototype[a] !== "function" &&
    ba(Array.prototype, a, {
      configurable: !0,
      writable: !0,
      value: function () {
        return da(aa(this));
      },
    });
  v = function () {};
};
var da = function (a) {
  v();
  a = { next: a };
  a[p.Symbol.iterator] = function () {
    return this;
  };
  return a;
};
const w = function (a) {
  const b =
    typeof Symbol !== "undefined" && Symbol.iterator && a[Symbol.iterator];
  return b ? b.call(a) : { next: aa(a) };
};
const ea = function (a) {
  if (!(a instanceof Array)) {
    a = w(a);
    for (var b, c = []; !(b = a.next()).done; ) c.push(b.value);
    a = c;
  }
  return a;
};
const fa =
  typeof Object.create === "function"
    ? Object.create
    : function (a) {
        const b = function () {};
        b.prototype = a;
        return new b();
      };
let ha;
if (typeof Object.setPrototypeOf === "function") ha = Object.setPrototypeOf;
else {
  let ia;
  a: {
    const ka = { i: !0 };
    const la = {};
    try {
      la.__proto__ = ka;
      ia = la.i;
      break a;
    } catch (a) {}
    ia = !1;
  }
  ha = ia
    ? function (a, b) {
        a.__proto__ = b;
        if (a.__proto__ !== b) throw new TypeError(a + " is not extensible");
        return a;
      }
    : null;
}
const ma = ha;
const x = function (a, b) {
  a.prototype = fa(b.prototype);
  a.prototype.constructor = a;
  if (ma) ma(a, b);
  else
    for (const c in b)
      if (c != "prototype")
        if (Object.defineProperties) {
          const d = Object.getOwnPropertyDescriptor(b, c);
          d && Object.defineProperty(a, c, d);
        } else a[c] = b[c];
  a.Gc = b.prototype;
};
const y = function (a, b) {
  if (b) {
    let c = p;
    a = a.split(".");
    for (var d = 0; d < a.length - 1; d++) {
      const e = a[d];
      e in c || (c[e] = {});
      c = c[e];
    }
    a = a[a.length - 1];
    d = c[a];
    b = b(d);
    b != d &&
      b != null &&
      ba(c, a, { configurable: !0, writable: !0, value: b });
  }
};
const na = function (a, b, c) {
  if (a == null) {
    throw new TypeError(
      "The 'this' value for String.prototype." +
        c +
        " must not be null or undefined"
    );
  }
  if (b instanceof RegExp)
    throw new TypeError(
      "First argument to String.prototype." +
        c +
        " must not be a regular expression"
    );
  return a + "";
};
const z = function (a, b) {
  return Object.prototype.hasOwnProperty.call(a, b);
};
const oa =
  typeof Object.assign === "function"
    ? Object.assign
    : function (a, b) {
        for (let c = 1; c < arguments.length; c++) {
          const d = arguments[c];
          if (d) for (const e in d) z(d, e) && (a[e] = d[e]);
        }
        return a;
      };
y("Object.assign", function (a) {
  return a || oa;
});
const pa = function (a, b) {
  v();
  a instanceof String && (a += "");
  let c = 0;
  var d = {
    next: function () {
      if (c < a.length) {
        const e = c++;
        return { value: b(e, a[e]), done: !1 };
      }
      d.next = function () {
        return { done: !0, value: void 0 };
      };
      return d.next();
    },
  };
  d[Symbol.iterator] = function () {
    return d;
  };
  return d;
};
y("Promise", function (a) {
  function b() {
    this.F = null;
  }
  function c(a) {
    return a instanceof e
      ? a
      : new e(function (b) {
          b(a);
        });
  }
  if (a) return a;
  b.prototype.Xa = function (a) {
    this.F == null && ((this.F = []), this.bc());
    this.F.push(a);
  };
  b.prototype.bc = function () {
    const a = this;
    this.Ya(function () {
      a.mc();
    });
  };
  const d = p.setTimeout;
  b.prototype.Ya = function (a) {
    d(a, 0);
  };
  b.prototype.mc = function () {
    for (; this.F && this.F.length; ) {
      const a = this.F;
      this.F = [];
      for (let b = 0; b < a.length; ++b) {
        const c = a[b];
        a[b] = null;
        try {
          c();
        } catch (m) {
          this.cc(m);
        }
      }
    }
    this.F = null;
  };
  b.prototype.cc = function (a) {
    this.Ya(function () {
      throw a;
    });
  };
  var e = function (a) {
    this.ea = 0;
    this.Ga = void 0;
    this.U = [];
    const b = this.va();
    try {
      a(b.resolve, b.reject);
    } catch (l) {
      b.reject(l);
    }
  };
  e.prototype.va = function () {
    function a(a) {
      return function (d) {
        c || ((c = !0), a.call(b, d));
      };
    }
    var b = this;
    var c = !1;
    return { resolve: a(this.yc), reject: a(this.Fa) };
  };
  e.prototype.yc = function (a) {
    if (a === this)
      this.Fa(new TypeError("A Promise cannot resolve to itself"));
    else if (a instanceof e) this.Ac(a);
    else {
      a: switch (typeof a) {
        case "object":
          var b = a != null;
          break a;
        case "function":
          b = !0;
          break a;
        default:
          b = !1;
      }
      b ? this.xc(a) : this.nb(a);
    }
  };
  e.prototype.xc = function (a) {
    let b = void 0;
    try {
      b = a.then;
    } catch (l) {
      this.Fa(l);
      return;
    }
    typeof b === "function" ? this.Bc(b, a) : this.nb(a);
  };
  e.prototype.Fa = function (a) {
    this.Fb(2, a);
  };
  e.prototype.nb = function (a) {
    this.Fb(1, a);
  };
  e.prototype.Fb = function (a, b) {
    if (this.ea != 0)
      throw Error(
        "Cannot settle(" +
          a +
          ", " +
          b +
          "): Promise already settled in state" +
          this.ea
      );
    this.ea = a;
    this.Ga = b;
    this.nc();
  };
  e.prototype.nc = function () {
    if (this.U != null) {
      for (let a = 0; a < this.U.length; ++a) g.Xa(this.U[a]);
      this.U = null;
    }
  };
  var g = new b();
  e.prototype.Ac = function (a) {
    const b = this.va();
    a.ia(b.resolve, b.reject);
  };
  e.prototype.Bc = function (a, b) {
    const c = this.va();
    try {
      a.call(b, c.resolve, c.reject);
    } catch (m) {
      c.reject(m);
    }
  };
  e.prototype.then = function (a, b) {
    function c(a, b) {
      return typeof a === "function"
        ? function (b) {
            try {
              d(a(b));
            } catch (H) {
              k(H);
            }
          }
        : b;
    }
    let d;
    let k;
    const g = new e(function (a, b) {
      d = a;
      k = b;
    });
    this.ia(c(a, d), c(b, k));
    return g;
  };
  e.prototype.catch = function (a) {
    return this.then(void 0, a);
  };
  e.prototype.ia = function (a, b) {
    function c() {
      switch (d.ea) {
        case 1:
          a(d.Ga);
          break;
        case 2:
          b(d.Ga);
          break;
        default:
          throw Error("Unexpected state: " + d.ea);
      }
    }
    var d = this;
    this.U == null ? g.Xa(c) : this.U.push(c);
  };
  e.resolve = c;
  e.reject = function (a) {
    return new e(function (b, c) {
      c(a);
    });
  };
  e.race = function (a) {
    return new e(function (b, d) {
      for (let e = w(a), k = e.next(); !k.done; k = e.next())
        c(k.value).ia(b, d);
    });
  };
  e.all = function (a) {
    const b = w(a);
    let d = b.next();
    return d.done
      ? c([])
      : new e(function (a, e) {
          function k(b) {
            return function (c) {
              g[b] = c;
              h--;
              h == 0 && a(g);
            };
          }
          var g = [];
          var h = 0;
          do {
            g.push(void 0),
              h++,
              c(d.value).ia(k(g.length - 1), e),
              (d = b.next());
          } while (!d.done);
        });
  };
  return e;
});
y("WeakMap", function (a) {
  function b() {}
  function c(a) {
    z(a, e) || ba(a, e, { value: new b() });
  }
  function d(a) {
    const d = Object[a];
    d &&
      (Object[a] = function (a) {
        if (a instanceof b) return a;
        c(a);
        return d(a);
      });
  }
  if (
    (function () {
      if (!a || !Object.seal) return !1;
      try {
        const b = Object.seal({});
        const c = Object.seal({});
        const d = new a([
          [b, 2],
          [c, 3],
        ]);
        if (d.get(b) != 2 || d.get(c) != 3) return !1;
        d.delete(b);
        d.set(c, 4);
        return !d.has(b) && d.get(c) == 4;
      } catch (q) {
        return !1;
      }
    })()
  )
    return a;
  var e = "$jscomp_hidden_" + Math.random();
  d("freeze");
  d("preventExtensions");
  d("seal");
  let g = 0;
  const h = function (a) {
    this.$ = (g += Math.random() + 1).toString();
    if (a) {
      a = w(a);
      for (var b; !(b = a.next()).done; ) (b = b.value), this.set(b[0], b[1]);
    }
  };
  h.prototype.set = function (a, b) {
    c(a);
    if (!z(a, e)) throw Error("WeakMap key fail: " + a);
    a[e][this.$] = b;
    return this;
  };
  h.prototype.get = function (a) {
    return z(a, e) ? a[e][this.$] : void 0;
  };
  h.prototype.has = function (a) {
    return z(a, e) && z(a[e], this.$);
  };
  h.prototype.delete = function (a) {
    return z(a, e) && z(a[e], this.$) ? delete a[e][this.$] : !1;
  };
  return h;
});
y("Map", function (a) {
  if (
    (function () {
      if (
        !a ||
        typeof a !== "function" ||
        !a.prototype.entries ||
        typeof Object.seal !== "function"
      )
        return !1;
      try {
        const b = Object.seal({ x: 4 });
        const c = new a(w([[b, "s"]]));
        if (
          c.get(b) != "s" ||
          c.size != 1 ||
          c.get({ x: 4 }) ||
          c.set({ x: 4 }, "t") != c ||
          c.size != 2
        )
          return !1;
        const d = c.entries();
        let e = d.next();
        if (e.done || e.value[0] != b || e.value[1] != "s") return !1;
        e = d.next();
        return e.done ||
          e.value[0].x != 4 ||
          e.value[1] != "t" ||
          !d.next().done
          ? !1
          : !0;
      } catch (t) {
        return !1;
      }
    })()
  )
    return a;
  v();
  const b = new WeakMap();
  const c = function (a) {
    this.Y = {};
    this.w = g();
    this.size = 0;
    if (a) {
      a = w(a);
      for (var b; !(b = a.next()).done; ) (b = b.value), this.set(b[0], b[1]);
    }
  };
  c.prototype.set = function (a, b) {
    a = a === 0 ? 0 : a;
    const c = d(this, a);
    c.list || (c.list = this.Y[c.id] = []);
    c.f
      ? (c.f.value = b)
      : ((c.f = { next: this.w, B: this.w.B, head: this.w, key: a, value: b }),
        c.list.push(c.f),
        (this.w.B.next = c.f),
        (this.w.B = c.f),
        this.size++);
    return this;
  };
  c.prototype.delete = function (a) {
    a = d(this, a);
    return a.f && a.list
      ? (a.list.splice(a.index, 1),
        a.list.length || delete this.Y[a.id],
        (a.f.B.next = a.f.next),
        (a.f.next.B = a.f.B),
        (a.f.head = null),
        this.size--,
        !0)
      : !1;
  };
  c.prototype.clear = function () {
    this.Y = {};
    this.w = this.w.B = g();
    this.size = 0;
  };
  c.prototype.has = function (a) {
    return !!d(this, a).f;
  };
  c.prototype.get = function (a) {
    return (a = d(this, a).f) && a.value;
  };
  c.prototype.entries = function () {
    return e(this, function (a) {
      return [a.key, a.value];
    });
  };
  c.prototype.keys = function () {
    return e(this, function (a) {
      return a.key;
    });
  };
  c.prototype.values = function () {
    return e(this, function (a) {
      return a.value;
    });
  };
  c.prototype.forEach = function (a, b) {
    for (var c = this.entries(), d; !(d = c.next()).done; ) {
      (d = d.value), a.call(b, d[1], d[0], this);
    }
  };
  c.prototype[Symbol.iterator] = c.prototype.entries;
  var d = function (a, c) {
    let d = c && typeof c;
    d == "object" || d == "function"
      ? b.has(c)
        ? (d = b.get(c))
        : ((d = "" + ++h), b.set(c, d))
      : (d = "p_" + c);
    const e = a.Y[d];
    if (e && z(a.Y, d))
      for (a = 0; a < e.length; a++) {
        const g = e[a];
        if ((c !== c && g.key !== g.key) || c === g.key)
          return { id: d, list: e, index: a, f: g };
      }
    return { id: d, list: e, index: -1, f: void 0 };
  };
  var e = function (a, b) {
    let c = a.w;
    return da(function () {
      if (c) {
        for (; c.head != a.w; ) c = c.B;
        for (; c.next != c.head; )
          return (c = c.next), { done: !1, value: b(c) };
        c = null;
      }
      return { done: !0, value: void 0 };
    });
  };
  var g = function () {
    const a = {};
    return (a.B = a.next = a.head = a);
  };
  var h = 0;
  return c;
});
y("Array.prototype.values", function (a) {
  return (
    a ||
    function () {
      return pa(this, function (a, c) {
        return c;
      });
    }
  );
});
y("String.prototype.startsWith", function (a) {
  return (
    a ||
    function (a, c) {
      const b = na(this, a, "startsWith");
      a += "";
      const e = b.length;
      const g = a.length;
      c = Math.max(0, Math.min(c | 0, b.length));
      for (var h = 0; h < g && c < e; ) if (b[c++] != a[h++]) return !1;
      return h >= g;
    }
  );
});
y("Object.is", function (a) {
  return (
    a ||
    function (a, c) {
      return a === c ? a !== 0 || 1 / a === 1 / c : a !== a && c !== c;
    }
  );
});
y("Array.prototype.includes", function (a) {
  return (
    a ||
    function (a, c) {
      let b = this;
      b instanceof String && (b = String(b));
      const e = b.length;
      c = c || 0;
      for (c < 0 && (c = Math.max(c + e, 0)); c < e; c++) {
        const g = b[c];
        if (g === a || Object.is(g, a)) return !0;
      }
      return !1;
    }
  );
});
y("String.prototype.includes", function (a) {
  return (
    a ||
    function (a, c) {
      return na(this, a, "includes").indexOf(a, c || 0) !== -1;
    }
  );
});
const qa = this;
let ra = (2147483648 * Math.random()) | 0;
const A = function (a, b, c) {
  return Math.min(Math.max(a, b), c);
};
const B = function (a) {
  this.a = a = void 0 === a ? {} : a;
};
B.prototype.tb = function () {};
p.Object.defineProperties(B, {
  H: {
    configurable: !0,
    enumerable: !0,
    get: function () {
      return {};
    },
  },
  c: {
    configurable: !0,
    enumerable: !0,
    get: function () {
      return {};
    },
  },
  ba: {
    configurable: !0,
    enumerable: !0,
    get: function () {
      return {};
    },
  },
  hb: {
    configurable: !0,
    enumerable: !0,
    get: function () {
      return {};
    },
  },
});
const C = function (a, b, c) {
  for (var d = [], e = 2; e < arguments.length; ++e) d[e - 2] = arguments[e];
  this.C = a;
  ea(d);
  this.wa = void 0 === b ? this.ob() : b;
  this.wa.tb();
  this.ub();
};
C.prototype.ob = function () {
  throw Error(
    "Subclasses must override getDefaultFoundation to return a properly configured foundation class"
  );
};
C.prototype.ub = function () {};
const sa = {
  Nb: "mdc-ripple-upgraded",
  Na: "mdc-ripple-upgraded--unbounded",
  Ka: "mdc-ripple-upgraded--background-focused",
  La: "mdc-ripple-upgraded--foreground-activation",
  Ma: "mdc-ripple-upgraded--foreground-deactivation",
};
const ta = {
  Tb: "--mdc-ripple-left",
  Ub: "--mdc-ripple-top",
  Qb: "--mdc-ripple-fg-size",
  Pb: "--mdc-ripple-fg-scale",
  Sb: "--mdc-ripple-fg-translate-start",
  Rb: "--mdc-ripple-fg-translate-end",
};
const ua = { Mb: 10, Lb: 0.6, Jb: 225, Kb: 150, Ob: 300 };
let va;
let wa;
const D = function () {
  var a = void 0 === a ? window : a;
  if (void 0 === wa) {
    let b = !1;
    try {
      a.document.addEventListener("test", null, {
        get passive() {
          return (b = !0);
        },
      });
    } catch (c) {}
    wa = b;
  }
  return wa ? { passive: !0 } : !1;
};
const xa = function () {
  for (
    var a = HTMLElement.prototype,
      b = ["matches", "webkitMatchesSelector", "msMatchesSelector"],
      c = "matches",
      d = 0;
    d < b.length;
    d++
  ) {
    const e = b[d];
    if (e in a) {
      c = e;
      break;
    }
  }
  return c;
};
const ya = ["touchstart", "pointerdown", "mousedown", "keydown"];
const za = ["touchend", "pointerup", "mouseup", "contextmenu"];
let Aa = [];
var E = function (a) {
  B.call(this, Object.assign(E.hb, a));
  const b = this;
  this.na = 0;
  this.m = { width: 0, height: 0 };
  this.D = Ba();
  this.wb = this.A = 0;
  this.$b = function (a) {
    return Ca(b, a);
  };
  this.ja = function () {
    return Da(b);
  };
  this.oc = function () {
    return Ea(b);
  };
  this.dc = function () {
    return Fa(b);
  };
  this.wc = function () {
    return b.ma();
  };
  this.Ia = { left: 0, top: 0 };
  this.lb = this.Wa = this.mb = 0;
  this.ta = !1;
  this.ac = function () {
    b.ta = !0;
    Ga(b);
  };
};
x(E, B);
var Ba = function () {
  return { la: !1, qb: !1, qa: !1, I: !1, ua: void 0, xa: !1 };
};
E.prototype.tb = function () {
  const a = this;
  let b = this.a.Za();
  Ha(this, b);
  if (b) {
    b = E.H;
    const c = b.Nb;
    const d = b.Na;
    requestAnimationFrame(function () {
      a.a.J(c);
      a.a.R() && (a.a.J(d), Ia(a));
    });
  }
};
var Ha = function (a, b) {
  b &&
    (ya.forEach(function (b) {
      a.a.da(b, a.$b);
    }),
    a.a.R() && a.a.Bb(a.wc));
  a.a.da("focus", a.oc);
  a.a.da("blur", a.dc);
};
const Ja = function (a, b) {
  b.type === "keydown"
    ? a.a.da("keyup", a.ja)
    : za.forEach(function (b) {
        a.a.Ab(b, a.ja);
      });
};
const Ka = function (a) {
  a.a.jb("keyup", a.ja);
  za.forEach(function (b) {
    a.a.ib(b, a.ja);
  });
};
var Ca = function (a, b) {
  if (!a.a.vb()) {
    const c = a.D;
    if (!c.la) {
      const d = a.zb;
      (d && void 0 !== b && d.type !== b.type) ||
        ((c.la = !0),
        (c.xa = void 0 === b),
        (c.ua = b),
        (c.qa = c.xa
          ? !1
          : void 0 !== b &&
            (b.type === "mousedown" ||
              b.type === "touchstart" ||
              b.type === "pointerdown")),
        void 0 !== b &&
        Aa.length > 0 &&
        Aa.some(function (b) {
          return a.a.cb(b);
        })
          ? La(a)
          : (void 0 !== b && (Aa.push(b.target), Ja(a, b)),
            (c.I = void 0 !== b && b.type === "keydown" ? a.a.za() : !0),
            c.I && Ma(a),
            requestAnimationFrame(function () {
              Aa = [];
              c.I ||
                void 0 === b ||
                (b.key !== " " && b.keyCode !== 32) ||
                ((c.I = void 0 !== b && b.type === "keydown" ? a.a.za() : !0),
                c.I && Ma(a));
              c.I || (a.D = Ba());
            })));
    }
  }
};
var Ma = function (a) {
  let b = E.c;
  const c = b.Sb;
  b = b.Rb;
  let d = E.H;
  const e = d.Ma;
  d = d.La;
  const g = E.ba.Jb;
  Ia(a);
  let h = "";
  let k = "";
  a.a.R() ||
    ((k = Na(a)),
    (h = k.Cc),
    (k = k.lc),
    (h = h.x + "px, " + h.y + "px"),
    (k = k.x + "px, " + k.y + "px"));
  a.a.N(c, h);
  a.a.N(b, k);
  clearTimeout(a.Wa);
  clearTimeout(a.lb);
  Oa(a);
  a.a.V(e);
  a.a.X();
  a.a.J(d);
  a.Wa = setTimeout(function () {
    return a.ac();
  }, g);
};
var Na = function (a) {
  let b = a.D;
  let c = b.ua;
  if (b.qa) {
    let d = a.a.pb();
    const e = a.a.X();
    b = d.x + e.left;
    d = d.y + e.top;
    c.type === "touchstart"
      ? ((b = c.changedTouches[0].pageX - b),
        (c = c.changedTouches[0].pageY - d))
      : ((b = c.pageX - b), (c = c.pageY - d));
    c = { x: b, y: c };
  } else c = { x: a.m.width / 2, y: a.m.height / 2 };
  c = { x: c.x - a.A / 2, y: c.y - a.A / 2 };
  return {
    Cc: c,
    lc: {
      x: a.m.width / 2 - a.A / 2,
      y: a.m.height / 2 - a.A / 2,
    },
  };
};
var Ga = function (a) {
  const b = E.H.Ma;
  const c = a.D;
  const d = c.la;
  (!c.qb && d) ||
    !a.ta ||
    (Oa(a),
    a.a.J(b),
    (a.lb = setTimeout(function () {
      a.a.V(b);
    }, ua.Kb)));
};
var Oa = function (a) {
  a.a.V(E.H.La);
  a.ta = !1;
  a.a.X();
};
var La = function (a) {
  a.zb = a.D.ua;
  a.D = Ba();
  setTimeout(function () {
    return (a.zb = void 0);
  }, E.ba.Ob);
};
var Da = function (a) {
  const b = a.D;
  if (b.la) {
    const c = Object.assign({}, b);
    b.xa
      ? (requestAnimationFrame(function () {
          const b = c.I;
          (c.qa || b) && Ga(a);
        }),
        La(a))
      : (Ka(a),
        requestAnimationFrame(function () {
          a.D.qb = !0;
          const b = c.I;
          (c.qa || b) && Ga(a);
          La(a);
        }));
  }
};
E.prototype.ma = function () {
  const a = this;
  this.na && cancelAnimationFrame(this.na);
  this.na = requestAnimationFrame(function () {
    Ia(a);
    a.na = 0;
  });
};
var Ia = function (a) {
  a.m = a.a.X();
  let b = Math.max(a.m.height, a.m.width);
  a.wb = a.a.R()
    ? b
    : Math.sqrt(Math.pow(a.m.width, 2) + Math.pow(a.m.height, 2)) + E.ba.Mb;
  a.A = Math.floor(b * E.ba.Lb);
  a.mb = a.wb / a.A;
  b = E.c;
  const c = b.Tb;
  const d = b.Ub;
  const e = b.Pb;
  a.a.N(b.Qb, a.A + "px");
  a.a.N(e, a.mb);
  a.a.R() &&
    ((a.Ia = {
      left: Math.round(a.m.width / 2 - a.A / 2),
      top: Math.round(a.m.height / 2 - a.A / 2),
    }),
    a.a.N(c, a.Ia.left + "px"),
    a.a.N(d, a.Ia.top + "px"));
};
var Ea = function (a) {
  requestAnimationFrame(function () {
    return a.a.J(E.H.Ka);
  });
};
var Fa = function (a) {
  requestAnimationFrame(function () {
    return a.a.V(E.H.Ka);
  });
};
p.Object.defineProperties(E, {
  H: {
    configurable: !0,
    enumerable: !0,
    get: function () {
      return sa;
    },
  },
  c: {
    configurable: !0,
    enumerable: !0,
    get: function () {
      return ta;
    },
  },
  ba: {
    configurable: !0,
    enumerable: !0,
    get: function () {
      return ua;
    },
  },
  hb: {
    configurable: !0,
    enumerable: !0,
    get: function () {
      return {
        Za: function () {},
        R: function () {},
        za: function () {},
        vb: function () {},
        J: function () {},
        V: function () {},
        cb: function () {},
        da: function () {},
        jb: function () {},
        Ab: function () {},
        ib: function () {},
        Bb: function () {},
        jc: function () {},
        N: function () {},
        X: function () {},
        pb: function () {},
      };
    },
  },
});
const F = function (a) {
  for (var b = [], c = 0; c < arguments.length; ++c) b[c - 0] = arguments[c];
  C.apply(this, ea(b));
  this.disabled = !1;
};
x(F, C);
const Pa = function (a) {
  const b = xa();
  return {
    Za: function () {
      let a = window;
      var b = void 0 === b ? !1 : b;
      let e = va;
      if (typeof va !== "boolean" || b) {
        if (a.CSS && typeof a.CSS.supports === "function") {
          e = a.CSS.supports("--css-vars", "yes");
          let g =
            a.CSS.supports("(--css-vars: yes)") &&
            a.CSS.supports("color", "#00000000");
          e || g
            ? ((g = a.document),
              (e = g.createElement("div")),
              (e.className = "mdc-ripple-surface--test-edge-var-bug"),
              g.body.appendChild(e),
              (a = a.getComputedStyle(e)),
              (a = a !== null && a.borderTopStyle === "solid"),
              e.remove(),
              (a = !a))
            : (a = !1);
          e = a;
          b || (va = e);
          b = e;
        } else b = void 0;
      } else b = e;
      return b;
    },
    R: function () {
      return a.Hb;
    },
    za: function () {
      return a.C[b](":active");
    },
    vb: function () {
      return a.disabled;
    },
    J: function (b) {
      return a.C.classList.add(b);
    },
    V: function (b) {
      return a.C.classList.remove(b);
    },
    cb: function (b) {
      return a.C.contains(b);
    },
    da: function (b, d) {
      return a.C.addEventListener(b, d, D());
    },
    jb: function (b, d) {
      return a.C.removeEventListener(b, d, D());
    },
    Ab: function (a, b) {
      return document.documentElement.addEventListener(a, b, D());
    },
    ib: function (a, b) {
      return document.documentElement.removeEventListener(a, b, D());
    },
    Bb: function (a) {
      return window.addEventListener("resize", a);
    },
    jc: function (a) {
      return window.removeEventListener("resize", a);
    },
    N: function (b, d) {
      return a.C.style.setProperty(b, d);
    },
    X: function () {
      return a.C.getBoundingClientRect();
    },
    pb: function () {
      return { x: window.pageXOffset, y: window.pageYOffset };
    },
  };
};
F.prototype.ma = function () {
  this.wa.ma();
};
F.prototype.ob = function () {
  return new E(Pa(this));
};
F.prototype.ub = function () {
  this.Hb = "mdcRippleIsUnbounded" in this.C.dataset;
};
p.Object.defineProperties(F.prototype, {
  Hb: {
    configurable: !0,
    enumerable: !0,
    get: function () {
      return this.Ib;
    },
    set: function (a) {
      this.Ib = !!a;
      a = this.wa;
      const b = E.H.Na;
      this.Ib ? a.a.J(b) : a.a.V(b);
    },
  },
});
const Qa = new Map();
const Ta = function (a, b) {
  let c = Ra;
  c = void 0 === c ? Sa : c;
  this.c = a;
  this.values = b;
  this.type = "html";
  this.Da = c;
};
function Ua(a) {
  let b = Qa.get(a.type);
  void 0 === b && ((b = new Map()), Qa.set(a.type, b));
  let c = b.get(a.c);
  if (void 0 === c) {
    c = document.createElement("template");
    for (var d = a.c.length - 1, e = "", g = !0, h = 0; h < d; h++) {
      const k = a.c[h];
      e += k;
      let l = k.lastIndexOf(">");
      l = k.indexOf("<", l + 1) > -1 ? k.length : l;
      g = l > -1 ? l < k.length : g;
      e += g ? Va : G;
    }
    e += a.c[d];
    c.innerHTML = e;
    c = new Wa(a, c);
    b.set(a.c, c);
  }
  return c;
}
var G = "{{lit-" + String(Math.random()).slice(2) + "}}";
var Va = "\x3c!--" + G + "--\x3e";
const Xa = new RegExp(G + "|" + Va);
const Ya =
  /[ \x09\x0a\x0c\x0d]([^\0-\x1F\x7F-\x9F \x09\x0a\x0c\x0d"'>=/]+)[ \x09\x0a\x0c\x0d]*=[ \x09\x0a\x0c\x0d]*(?:[^ \x09\x0a\x0c\x0d"'`<>=]*|"[^"]*|'[^']*)$/;
const Za = function (a, b, c, d, e) {
  this.type = a;
  this.index = b;
  this.name = c;
  this.Ea = d;
  this.c = e;
};
var Wa = function (a, b) {
  this.oa = [];
  this.element = b;
  b = document.createTreeWalker(this.element.content, 133, null, !1);
  for (var c = -1, d = 0, e = [], g, h; b.nextNode(); ) {
    c++;
    g = h;
    const k = (h = b.currentNode);
    if (k.nodeType === 1) {
      if (k.hasAttributes()) {
        g = k.attributes;
        for (var l = 0, m = 0; m < g.length; m++)
          g[m].value.indexOf(G) >= 0 && l++;
        for (; l-- > 0; ) {
          m = Ya.exec(a.c[d])[1];
          var q = g.getNamedItem(m);
          const t = q.value.split(Xa);
          this.oa.push(new Za("attribute", c, q.name, m, t));
          k.removeAttribute(q.name);
          d += t.length - 1;
        }
      }
    } else if (k.nodeType === 3) {
      if (((l = k.nodeValue), !(l.indexOf(G) < 0))) {
        g = k.parentNode;
        l = l.split(Xa);
        m = l.length - 1;
        d += m;
        for (q = 0; q < m; q++) {
          g.insertBefore(
            l[q] === ""
              ? document.createComment("")
              : document.createTextNode(l[q]),
            k
          ),
            this.oa.push(new Za("node", c++));
        }
        g.insertBefore(
          l[m] === ""
            ? document.createComment("")
            : document.createTextNode(l[m]),
          k
        );
        e.push(k);
      }
    } else
      k.nodeType === 8 &&
        k.nodeValue === G &&
        ((h = k.parentNode),
        (l = k.previousSibling),
        l === null || l !== g || l.nodeType !== Node.TEXT_NODE
          ? h.insertBefore(document.createComment(""), k)
          : c--,
        this.oa.push(new Za("node", c++)),
        e.push(k),
        k.nextSibling === null
          ? h.insertBefore(document.createComment(""), k)
          : c--,
        (h = g),
        d++);
  }
  a = w(e);
  for (b = a.next(); !b.done; b = a.next())
    (b = b.value), b.parentNode.removeChild(b);
};
const J = function (a, b) {
  return typeof b === "function" && !0 === b.Vb
    ? (b(a), I)
    : b === null
    ? void 0
    : b;
};
const $a = function (a) {
  a.Vb = !0;
  return a;
};
var I = {};
const ab = function (a) {
  return a === null || !(typeof a === "object" || typeof a === "function");
};
const K = function (a, b, c, d) {
  this.aa = a;
  this.element = b;
  this.name = c;
  this.c = d;
  this.size = d.length - 1;
  this.ra = [];
};
K.prototype.Sa = function (a, b) {
  for (var c = this.c, d = c.length - 1, e = "", g = 0; g < d; g++) {
    e += c[g];
    let h = J(this, a[b + g]);
    u();
    v();
    if (
      h &&
      h !== I &&
      (Array.isArray(h) || (typeof h !== "string" && h[Symbol.iterator]))
    ) {
      h = w(h);
      for (let k = h.next(); !k.done; k = h.next()) e += k.value;
    } else e += h;
  }
  return e + c[d];
};
K.prototype.Pa = function (a, b) {
  for (let c = b; c < b + this.size; c++)
    if (this.ra[c] !== a[c] || !ab(a[c])) return !1;
  return !0;
};
K.prototype.o = function (a, b) {
  if (!this.Pa(a, b)) {
    const c = this.c;
    c.length === 2 && c[0] === "" && c[1] === ""
      ? ((b = J(this, a[b])), Array.isArray(b) && (b = b.join("")))
      : (b = this.Sa(a, b));
    b !== I && this.element.setAttribute(this.name, b);
    this.ra = a;
  }
};
const bb = function (a, b, c) {
  this.aa = a;
  this.W = b;
  this.l = c;
  this.g = void 0;
};
f = bb.prototype;
f.o = function (a) {
  a = J(this, a);
  a !== I &&
    (ab(a)
      ? a !== this.g && this.Va(a)
      : a instanceof Ta
      ? this.Zb(a)
      : (u(),
        v(),
        Array.isArray(a) || a[Symbol.iterator]
          ? this.Xb(a)
          : a instanceof Node
          ? this.sa(a)
          : void 0 !== a.then
          ? this.Yb(a)
          : this.Va(a)));
};
f.Ra = function (a) {
  this.l.parentNode.insertBefore(a, this.l);
};
f.sa = function (a) {
  this.g !== a && (this.clear(), this.Ra(a), (this.g = a));
};
f.Va = function (a) {
  const b = this.W.nextSibling;
  a = void 0 === a ? "" : a;
  b === this.l.previousSibling && b.nodeType === Node.TEXT_NODE
    ? (b.textContent = a)
    : this.sa(document.createTextNode(a));
  this.g = a;
};
f.Zb = function (a) {
  let b = this.aa.Qa(a);
  this.g && this.g.pa === b
    ? (b = this.g)
    : ((b = new cb(b, a.Da, this.aa.Qa)), this.sa(b.Oa()), (this.g = b));
  b.update(a.values);
};
f.Xb = function (a) {
  Array.isArray(this.g) || (this.clear(), (this.g = []));
  const b = this.g;
  let c = 0;
  a = w(a);
  for (let d = a.next(); !d.done; d = a.next()) {
    d = d.value;
    let e = b[c];
    void 0 === e &&
      ((e = this.W),
      c > 0 && ((e = b[c - 1].l = document.createTextNode("")), this.Ra(e)),
      (e = new bb(this.aa, e, this.l)),
      b.push(e));
    e.o(d);
    c++;
  }
  c === 0
    ? (this.clear(), (this.g = void 0))
    : c < b.length &&
      ((a = b[c - 1]),
      (b.length = c),
      this.clear(a.l.previousSibling),
      (a.l = this.l));
};
f.Yb = function (a) {
  const b = this;
  this.g = a;
  a.then(function (c) {
    b.g === a && b.o(c);
  });
};
f.clear = function (a) {
  a = void 0 === a ? this.W : a;
  db(this.W.parentNode, a.nextSibling, this.l);
};
var Sa = function (a, b, c) {
  if (b.type === "attribute") return new K(a, c, b.name, b.c);
  if (b.type === "node") return new bb(a, c, c.nextSibling);
  throw Error("Unknown part type " + b.type);
};
var cb = function (a, b, c) {
  this.Ua = [];
  this.pa = a;
  this.Ta = b;
  this.Qa = c;
};
cb.prototype.update = function (a) {
  for (let b = 0, c = w(this.Ua), d = c.next(); !d.done; d = c.next())
    (d = d.value)
      ? void 0 === d.size
        ? (d.o(a[b]), b++)
        : (d.o(a, b), (b += d.size))
      : b++;
};
cb.prototype.Oa = function () {
  const a = this.pa.element.content.cloneNode(!0);
  const b = this.pa.oa;
  if (b.length > 0)
    for (
      let c = document.createTreeWalker(a, 133, null, !1), d = -1, e = 0;
      e < b.length;
      e++
    ) {
      const g = b[e];
      const h = g.index !== -1;
      if (h) for (; d < g.index; ) d++, c.nextNode();
      this.Ua.push(h ? this.Ta(this, g, c.currentNode) : void 0);
    }
  return a;
};
var db = function (a, b, c) {
  for (c = void 0 === c ? null : c; b !== c; ) {
    const d = b.nextSibling;
    a.removeChild(b);
    b = d;
  }
};
const L = function (a, b) {
  for (var c = [], d = 1; d < arguments.length; ++d) c[d - 1] = arguments[d];
  return new Ta(a, c);
};
var Ra = function (a, b, c) {
  if (b.type === "attribute") {
    if (b.Ea.substr(0, 3) === "on-") return new eb(a, c, b.Ea.slice(3));
    const d = b.name.substr(b.name.length - 1);
    return d === "$"
      ? new K(a, c, b.name.slice(0, -1), b.c)
      : d === "?"
      ? new fb(a, c, b.name.slice(0, -1), b.c)
      : new gb(a, c, b.Ea, b.c);
  }
  return Sa(a, b, c);
};
var fb = function (a) {
  K.apply(this, arguments);
};
x(fb, K);
fb.prototype.o = function (a, b) {
  const c = this.c;
  if (c.length === 2 && c[0] === "" && c[1] === "")
    (a = J(this, a[b])),
      a !== I &&
        (a
          ? this.element.setAttribute(this.name, "")
          : this.element.removeAttribute(this.name));
  else throw Error("boolean attributes can only contain a single expression");
};
var gb = function (a) {
  K.apply(this, arguments);
};
x(gb, K);
gb.prototype.o = function (a, b) {
  const c = this.c;
  this.Pa(a, b) ||
    ((b =
      c.length === 2 && c[0] === "" && c[1] === ""
        ? J(this, a[b])
        : this.Sa(a, b)),
    b !== I && (this.element[this.name] = b),
    (this.ra = a));
};
var eb = function (a, b, c) {
  this.aa = a;
  this.element = b;
  this.kb = c;
};
eb.prototype.o = function (a) {
  a = J(this, a);
  a !== this.O &&
    (a == null
      ? this.element.removeEventListener(this.kb, this)
      : this.O == null && this.element.addEventListener(this.kb, this),
    (this.O = a));
};
eb.prototype.handleEvent = function (a) {
  typeof this.O === "function"
    ? this.O.call(this.element, a)
    : typeof this.O.handleEvent === "function" && this.O.handleEvent(a);
};
function M(a, b, c) {
  if (isNaN(a) || a < 0 || a > b)
    throw new RangeError(a + " for " + c + " is not between 0 and " + b);
}
const O = Math.pow(2, -16);
const ib = function (a) {
  return 1 - a.alpha < O ? a : new P(a.red, a.green, a.blue);
};
const nb = function (a) {
  if (!/^[a-fA-F0-9]{3,8}$/.test(a))
    throw Error("Invalid hex color string: " + a);
  if (a.length === 3 || a.length === 4) {
    var b = /^(.)(.)(.)(.)?$/
      .exec(a)
      .slice(1, 5)
      .map(function (a) {
        return a ? a + a : "ff";
      });
  } else if (a.length === 6 || a.length === 8)
    (b = /^(..)(..)(..)(..)?$/.exec(a).slice(1, 5)),
      void 0 === b[3] && (b[3] = "ff");
  else throw Error("Invalid hex color string: " + a);
  a = mb(b[0]) / 255;
  const c = mb(b[1]) / 255;
  const d = mb(b[2]) / 255;
  b = mb(b[3]) / 255;
  return new P(a, c, d, b);
};
const ob = new P(1, 1, 1);
const pb = new P(0, 0, 0);
function mb(a) {
  if (!/^[a-fA-F0-9]+$/.test(a)) throw Error("Invalid hex string: " + a);
  return parseInt(a, 16);
}
function hb(a) {
  a = a.toString(16);
  return a.length >= 2 ? a : "0" + a;
}
function Ob(a) {
  var b = void 0 === b ? 4.5 : b;
  const c = jb(ob, a);
  if (c >= b) return 0;
  a = jb(pb, a);
  return a >= b ? 1 : c > a ? 0 : 1;
}
X(ob);
qa.__materialGlobalErrorHandler ||
  (qa.__materialGlobalErrorHandler = function (a) {
    throw a;
  });
function Rb(a) {
  for (var b = [], c = 0; c < arguments.length; ++c) b[c - 0] = arguments[c];
  return b
    .reduce(function (a, b) {
      return typeof b === "string"
        ? a.concat(b)
        : b && b[1]
        ? a.concat(b[0])
        : a;
    }, [])
    .join(" ");
}
const Sb = function (a) {
  this.app = a;
};
const Tb = function (a, b) {
  this.T = a;
  this.ca = b;
  this.ha = !1;
};
const Ub = function (a) {
  a.ha ||
    (document.addEventListener("mousemove", a.T),
    document.addEventListener("mouseup", a.ca),
    (a.ha = !0));
};
Tb.prototype.detach = function () {
  this.ha &&
    (document.removeEventListener("mousemove", this.T),
    document.removeEventListener("mouseup", this.ca),
    (this.ha = !1));
};
const Vb = function (a, b) {
  a.preventDefault();
  let c = a.clientX;
  let d = a.clientY;
  const e = function (a) {
    if (c !== a.clientX || d !== a.clientY)
      (c = a.clientX), (d = a.clientY), b.T(a.clientX, a.clientY);
  };
  var g = new Tb(e, function (a) {
    e(a);
    g.detach();
    b.ca();
  });
  Ub(g);
  b.T(a.clientX, a.clientY);
  return g;
};
function Wb(a, b) {
  return $a(function (c) {
    void 0 !== b
      ? c.element.setAttribute(a, String(b))
      : c.element.removeAttribute(a);
  });
}
function Yb(a) {
  const b = a;
  const c = b.value;
  return L(
    Xb,
    b.G,
    Wb("maxlength", b.maxLength),
    Wb("aria-label", b.ga),
    $a(function (a) {
      a = a.element;
      return c !== a.value ? (a.value = c) : c;
    }),
    b.L,
    b.S,
    b.Ca
  );
}
const cc = function (a) {
  Sb.apply(this, arguments);
};
x(cc, Sb);
const dc = function (a, b, c) {
  a.K && a.K.detach();
  const d = b.currentTarget;
  a.K = Vb(b, {
    T: function (b, g) {
      const e = d.getBoundingClientRect();
      b = new U(
        c.hue,
        A((b - e.left) / e.width, 0, 1),
        1 - A((g - e.top) / e.height, 0, 1),
        c.alpha
      );
      a.fb(b);
    },
    ca: function () {
      a.K = void 0;
      a.eb();
    },
  });
};
const ec = function (a, b, c) {
  a.K && a.K.detach();
  const d = b.currentTarget;
  a.K = Vb(b, {
    T: function (b) {
      const e = d.getBoundingClientRect();
      b = new U(
        360 * A((b - e.left) / e.width, 0, 1),
        c.saturation,
        c.value,
        c.alpha
      );
      a.fb(b);
    },
    ca: function () {
      a.K = void 0;
      a.eb();
    },
  });
};
cc.prototype.u = function (a) {
  const b = this;
  const c = a.color;
  let d = a.L;
  this.eb = a.S;
  this.fb = d;
  d = (c.hue / 360) * 100;
  const e = 100 * c.saturation;
  const g = 100 - 100 * c.value;
  const h = S(new U(c.hue, 1, 1));
  const k = S(c);
  return L(
    bc,
    function (a) {
      return dc(b, a, c);
    },
    "background-color: hsl(" + c.hue + ", 100%, 50%);",
    fc({ G: "color-picker-satval__thumb", color: k, Ba: e, Ha: g }),
    function (a) {
      return ec(b, a, c);
    },
    fc({ G: "color-picker-hue__thumb", color: h, Ba: d, Ha: 50 }),
    gc(a)
  );
};
var gc = function (a) {
  const b = a.color;
  let c = a.rb;
  let d = a.Ec;
  const e = a.rc;
  const g = a.hueText;
  const h = a.saturationText;
  const k = a.lightnessText;
  const l = a.sc;
  let m = a.Fc;
  const q = a.L;
  let t = S(b);
  t = Yb({
    value: void 0 !== c ? c : Q(t),
    G: "text-field color-picker-inputs__hex",
    maxLength: 7,
    ga: "Hex code",
    L:
      e &&
      function (a) {
        e(a.target.value);
      },
    S: d,
  });
  const n = sb(b);
  const r = qb(n);
  c = Yb({
    value: void 0 !== g ? g : r.hue,
    G: "text-field color-picker-inputs__hsl-input",
    ga: "Hue",
    L:
      l &&
      function (a) {
        l(a.target.value, h, k);
      },
    S: m,
    Ca: function (a) {
      a = hc(a);
      a = a < 0 ? Math.floor(a) : Math.ceil(a);
      a = new U(A(b.hue + a, 0, 360), b.saturation, b.value, b.alpha);
      q(a);
    },
  });
  d = Yb({
    value: void 0 !== h ? h : r.saturation,
    G: "text-field color-picker-inputs__hsl-input",
    ga: "Saturation",
    L:
      l &&
      function (a) {
        l(g, a.target.value, k);
      },
    S: m,
    Ca: function (a) {
      a = ub(
        new T(n.hue, A(100 * n.saturation + hc(a), 0, 100) / 100, n.b, n.alpha)
      );
      q(a);
    },
  });
  m = Yb({
    value: void 0 !== k ? k : r.b,
    G: "text-field color-picker-inputs__hsl-input",
    ga: "Lightness",
    L:
      l &&
      function (a) {
        l(g, h, a.target.value);
      },
    S: m,
    Ca: function (a) {
      a = ub(
        new T(n.hue, n.saturation, A(100 * n.b + hc(a), 0, 100) / 100, n.alpha)
      );
      q(a);
    },
  });
  t = [t];
  a.Dc || t.push(L(ac, c, L($b, "H"), d, L($b, "S"), m, L($b, "L")));
  return t;
};
function hc(a) {
  const b = a.keyCode;
  const c = a.altKey;
  let d = 1;
  a.shiftKey && (d *= 10);
  c && (d *= 0.1);
  return b === 38 ? 1 * d : b === 40 ? -1 * d : 0;
}
function fc(a) {
  const b = a;
  const c = b.G;
  return L(
    Zb,
    c,
    "left: " + b.Ba + "%; top: " + b.Ha + "%;",
    c + "__inner",
    "background-color: " + b.color.M() + ";"
  );
}
const ic = [
  '\n      <div class="color-palette-picker__cell"\n          title="',
  '"\n          style$=',
  '\n          on-click="',
  '">\n        ',
  "\n      </div>\n    ",
];
ic.raw = [
  '\n      <div class="color-palette-picker__cell"\n          title="',
  '"\n          style$=',
  '\n          on-click="',
  '">\n        ',
  "\n      </div>\n    ",
];
const jc = [
  '\n    <div class="color-palette-picker__row">\n      ',
  "\n    </div>\n  ",
];
jc.raw = [
  '\n    <div class="color-palette-picker__row">\n      ',
  "\n    </div>\n  ",
];
function kc(a) {
  let b = a;
  const c = b.tc;
  const d = b.uc;
  const e = b.selectedColor;
  const g = b.qc;
  b = c
    .map(function (a, b) {
      const h = void 0 !== e && a.ka(e);
      if (b < 0 || b > 9)
        throw new RangeError("colorIndex must be between 0 and 9, inclusive");
      return lc(a, h, b === 0 ? 50 : 100 * b, d, function () {
        return g(c, b);
      });
    })
    .reverse();
  return L(jc, b);
}
function lc(a, b, c, d, e) {
  const g = { G: "color-palette-picker__thumb", color: a, Ba: 50, Ha: 50 };
  return L(
    ic,
    d + " " + c,
    "background-color: " + a.M() + ";",
    e,
    b ? fc(g) : void 0
  );
}
const mc = function (a, b, c, d) {
  const e = this;
  this.bb = a;
  this.hc = b;
  this.store = c;
  this.vc = d;
  this.kc = this.ya = !1;
  c.subscribe(function () {
    const a = e.store.getState();
    a !== e.pc && ((e.pc = a), e.u());
  });
};
mc.prototype.u = function () {
  const a = this;
  this.ya &&
    console.warn("render() called during a render(). This is probably a bug.");
  return this.fa
    ? this.fa
    : (this.fa = Promise.resolve().then(function () {
        if (!a.kc) {
          try {
            a.ya = !0;
            try {
              const b = a.hc.u(a.store.getState());
              const c = a.bb;
              var d = void 0 === d ? Ua : d;
              const e = d(b);
              let g = c.Wb;
              if (void 0 !== g && g.pa === e && g.Ta === b.Da)
                g.update(b.values);
              else {
                g = new cb(e, b.Da, d);
                c.Wb = g;
                const h = g.Oa();
                g.update(b.values);
                db(c, c.firstChild);
                c.appendChild(h);
              }
            } catch (k) {
              qa.__materialGlobalErrorHandler(k);
            } finally {
              a.ya = !1;
            }
            a.vc(a.bb);
          } finally {
            a.fa = void 0;
          }
        }
      }));
};
function nc(a) {
  return function () {
    return function (b) {
      return oc(b, a);
    };
  };
}
function oc(a, b) {
  return function (c) {
    const d = a(c);
    b(c);
    return d;
  };
}
const Y = function (a, b, c, d) {
  const e = this;
  this.Z = d;
  this.Aa = { width: 0, height: 0 };
  this.zc = new a(pc(this));
  this.store = this.createStore(c);
  this.Db = new mc(b, this.zc, this.store, function (a) {
    if (a.scrollWidth !== e.Aa.width || a.scrollHeight !== e.Aa.height)
      (a = { width: a.scrollWidth, height: a.scrollHeight }),
        e.Z.panelSizeChanged(a),
        (e.Aa = a);
  });
};
Y.prototype.start = function () {
  this.Z.stateChanged(this.store.getState());
  return this.u();
};
Y.prototype.u = function () {
  return this.Db.u();
};
Y.prototype.createStore = function (a) {
  const b = this;
  const c = Redux.applyMiddleware(
    nc(function (a) {
      b.Z.actionDispatched(a);
    })
  );
  const d = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || Redux.compose;
  const e = this.getInitialState();
  const g = Redux.createStore(a, e, d(c));
  g.subscribe(function () {
    return b.Z.stateChanged(g.getState());
  });
  return g;
};
Y.prototype.getInitialState = function () {
  return this.Z.getInitialState();
};
var pc = function (a) {
  return {
    dispatch: function (b) {
      b = w(Array.isArray(b) ? b : [b]);
      for (let c = b.next(); !c.done; c = b.next()) a.store.dispatch(c.value);
    },
    u: function () {
      a.Db.u();
    },
  };
};
function qc(a) {
  return { type: "SET_PRIMARY_COLOR", primaryColor: a };
}
function rc(a) {
  return { type: "SET_SECONDARY_COLOR", secondaryColor: a };
}
function sc(a) {
  return { type: "COPY_TO_CLIPBOARD", selectedColor: a };
}
function tc(a) {
  return { type: "EXPAND_COLOR_MENU", openColorMenu: a };
}
const uc = /^[a-fA-F0-9]{3,6}$/;
function vc(a, b, c) {
  const d = { type: "SET_COLOR_HEX", hex: a };
  a.startsWith("#") && (a = a.slice(1));
  return !uc.test(a) || (a.length !== 3 && a.length !== 6)
    ? [d]
    : ((a = nb(a)), [c(a, b), d]);
}
function wc(a, b, c) {
  const d = {
    type: "SET_COLOR_HSL_TEXT",
    hueText: a.hue,
    saturationText: a.saturation,
    lightnessText: a.b,
  };
  let e = xc(a.hue);
  const g = xc(a.saturation);
  a = xc(a.b);
  return e >= 0 && e <= 360 && g >= 0 && g <= 100 && a >= 0 && a <= 100
    ? ((e = new T(e, g / 100, a / 100)), [c(e, b), d])
    : [d];
}
function xc(a) {
  a = a.trim();
  return a.length ? Number(a) : NaN;
}
const yc = [
  '\n      <div id="',
  '" class$="',
  '"\n          on-transitionend="',
  '">\n        ',
  "\n      </div>\n    ",
];
yc.raw = [
  '\n      <div id="',
  '" class$="',
  '"\n          on-transitionend="',
  '">\n        ',
  "\n      </div>\n    ",
];
const zc = function () {};
function Ac(a) {
  const b = "goog_" + ra++;
  let c = zc;
  const d = function (d) {
    const e = d.target;
    e.id === b && (a.xb && a.xb(d), e.classList.contains(a.sb) && c());
  };
  return function (e) {
    const g = $a(function (a) {
      let b = a.W.nextSibling === a.l;
      e
        ? ((c = zc), a.o(e))
        : b ||
          ((b = new Promise(function (a) {
            c = function () {
              a(e);
            };
          })),
          a.o(b));
    });
    const h = Rb(a.ic, [a.Gb || "", !!a.Gb && !!e], [a.sb, !e]);
    return L(yc, b, h, d, g);
  };
}
const Bc = tb(nb("6202EE"));
function Cc(a, b) {
  let c = a.Ja;
  c = void 0 === c ? Dc : c;
  c =
    b.type === "EXPAND_COLOR_MENU"
      ? Object.assign({}, c, { P: b.openColorMenu })
      : b.type === "INITIAL_LOAD"
      ? Object.assign({}, c, { P: !0 })
      : c;
  let d = a.$a;
  d = void 0 === d ? Ec : d;
  d =
    b.type === "COPY_TO_CLIPBOARD"
      ? Object.assign({}, d, { ab: b.selectedColor })
      : d;
  return { Ja: c, $a: d, colors: Fc(a.colors, b) };
}
var Dc = { P: !1 };
var Ec = { ab: "" };
const Gc = {
  primaryColor:
    new // Change default primary color here. Original was white (0,0,1).
    U(264, 0.99, 0.932),
  secondaryColor: void 0,
  s: 0,
  h: void 0,
};
function Fc(a, b) {
  a = void 0 === a ? Gc : a;
  switch (b.type) {
    case "INITIAL_LOAD":
      return { primaryColor: Bc, secondaryColor: void 0, s: 0, h: void 0 };
    case "SHOW_COLOR_PICKER":
      return Object.assign({}, a, {
        s: b.isPrimaryColor ? 1 : 2,
        h: Hc(
          b.isPrimaryColor ? a.primaryColor : a.secondaryColor || new U(0, 0, 1)
        ),
      });
    case "HIDE_COLOR_PICKER":
      return Object.assign({}, a, { s: 0, h: void 0 });
    case "SET_PRIMARY_COLOR":
      return Object.assign({}, a, {
        primaryColor: b.primaryColor,
        h: a.s === 1 ? Hc(b.primaryColor) : a.h,
      });
    case "SET_SECONDARY_COLOR":
      return Object.assign({}, a, {
        secondaryColor: b.secondaryColor,
        h: a.s === 2 ? Hc(b.secondaryColor) : a.h,
      });
    case "REMOVE_SECONDARY_COLOR":
      return Object.assign({}, a, {
        secondaryColor: void 0,
        h: a.s === 2 ? void 0 : a.h,
      });
    default:
      if (void 0 !== a.h) {
        a: {
          const c = a.h;
          switch (b.type) {
            case "SET_COLOR_HEX":
              b = Object.assign({}, c, { rb: b.hex });
              break a;
            case "SET_COLOR_HSL_TEXT":
              b = Object.assign({}, c, {
                hueText: b.hueText,
                saturationText: b.saturationText,
                lightnessText: b.lightnessText,
              });
              break a;
          }
          b = c;
        }
        if (b !== a.h) return Object.assign({}, a, { h: b });
      }
      return a;
  }
}
function Hc(a) {
  var b = void 0 === b ? S(a) : b;
  const c = qb(sb(a));
  return {
    rb: Q(b),
    hueText: c.hue,
    saturationText: c.saturation,
    lightnessText: c.b,
    color: a,
  };
}
function Ic(a, b) {
  return $a(function (c) {
    c.o(a);
    for (let d = c.W.nextSibling; d && d !== c.l; ) {
      if (d instanceof Element && !d.classList.contains("mdc-ripple-surface")) {
        d.classList.add("mdc-ripple-surface");
        const e = new F(d);
        b && b(e);
      }
      d = d.nextSibling;
    }
  });
}
const Jc =
  '\n      <input type="text" id="clipboardcopy" readonly="true">\n      <div class="color-tool" on-click=";">\n        <div class="tool-title">Color palettes</div>\n        ;\n        ;\n        ;\n        ;\n      </div>\n      <div class="mobile-message">\n        <div class="mobile-message__logo-container">\n          <div class="mobile-message__logo"></div>\n        </div>\n        <div class="mobile-message__title">\n          <i class="mobile-message__title-icon material-icons">info_outline</i>\n          <span class="mobile-message__title-message">\n            Demos only available at larger screen size\n          </span>\n        </div>\n      </div>\n    '.split(
    ";"
  );
Jc.raw =
  '\n      <input type="text" id="clipboardcopy" readonly="true">\n      <div class="color-tool" on-click=";">\n        <div class="tool-title">Color palettes</div>\n        ;\n        ;\n        ;\n        ;\n      </div>\n      <div class="mobile-message">\n        <div class="mobile-message__logo-container">\n          <div class="mobile-message__logo"></div>\n        </div>\n        <div class="mobile-message__title">\n          <i class="mobile-message__title-icon material-icons">info_outline</i>\n          <span class="mobile-message__title-message">\n            Demos only available at larger screen size\n          </span>\n        </div>\n      </div>\n    '.split(
    ";"
  );
const Kc = [
  '<div class$="clipboard-confirmation ',
  '" on-animationend="',
  '">Color copied to clipboard</div>',
];
Kc.raw = [
  '<div class$="clipboard-confirmation ',
  '" on-animationend="',
  '">Color copied to clipboard</div>',
];
const Lc = [
  '\n      <div class="color-picker-panel__remove">\n        ',
  "\n      </div>\n    ",
];
Lc.raw = [
  '\n      <div class="color-picker-panel__remove">\n        ',
  "\n      </div>\n    ",
];
const Mc =
  '\n          <button class="color-picker-panel__remove-button"\n              data-disabled$=";"\n              data-g-category$=;\n              data-g-action$=;\n              data-g-label$="; - remove"\n              on-click=";">\n            <i class="material-icons">format_color_reset</i>\n            <span>Remove color</span>\n          </button>\n        '.split(
    ";"
  );
Mc.raw =
  '\n          <button class="color-picker-panel__remove-button"\n              data-disabled$=";"\n              data-g-category$=;\n              data-g-action$=;\n              data-g-label$="; - remove"\n              on-click=";">\n            <i class="material-icons">format_color_reset</i>\n            <span>Remove color</span>\n          </button>\n        '.split(
    ";"
  );
const Nc = [
  '\n        <div class="color-picker-panel__label">',
  '</div>\n        <div class="color-picker-panel__swatch-selector">\n          ',
  "\n        </div>\n        ",
  "\n        ",
  "\n      </div>\n      ",
];
Nc.raw = [
  '\n        <div class="color-picker-panel__label">',
  '</div>\n        <div class="color-picker-panel__swatch-selector">\n          ',
  "\n        </div>\n        ",
  "\n        ",
  "\n      </div>\n      ",
];
const Oc =
  '\n    <div class$=";">\n      <div class="utility-panel__label" on-click=";"\n          data-g-category$=;\n          data-g-action$=;\n          data-g-label$=;>\n        Colors <i class="utility-panel__label-icon material-icons">remove</i></div>\n      <div class="content__color">\n        <div class="color-row">\n          ;\n          ;\n        </div>\n      </div>\n      <div class="content__info">\n        <a class="external__link" href=";" target="_blank"\n          data-g-category$=;\n          data-g-action$=;\n          data-g-label$="open external color tool">\n          <span class="external__logo">View in color tool</span>\n          <i class="external__link--open material-icons">open_in_new</i>\n        </a>\n        <div class="external-copy">\n          See selected colors applied to UI and check accessibility.\n        </div>\n      </div>\n    </div>\n    '.split(
    ";"
  );
Oc.raw =
  '\n    <div class$=";">\n      <div class="utility-panel__label" on-click=";"\n          data-g-category$=;\n          data-g-action$=;\n          data-g-label$=;>\n        Colors <i class="utility-panel__label-icon material-icons">remove</i></div>\n      <div class="content__color">\n        <div class="color-row">\n          ;\n          ;\n        </div>\n      </div>\n      <div class="content__info">\n        <a class="external__link" href=";" target="_blank"\n          data-g-category$=;\n          data-g-action$=;\n          data-g-label$="open external color tool">\n          <span class="external__logo">View in color tool</span>\n          <i class="external__link--open material-icons">open_in_new</i>\n        </a>\n        <div class="external-copy">\n          See selected colors applied to UI and check accessibility.\n        </div>\n      </div>\n    </div>\n    '.split(
    ";"
  );
const Pc =
  '\n      <div class$="utility-panel__color-entry ;"\n          style$=";"\n          on-click=";">\n        <div class="utility-panel__large-letter"\n            style$="color: ;">;</div>\n        <div class="utility-panel__subtitle"\n            style$="color: ;">;</div>\n        ;\n      </div>\n    '.split(
    ";"
  );
Pc.raw =
  '\n      <div class$="utility-panel__color-entry ;"\n          style$=";"\n          on-click=";">\n        <div class="utility-panel__large-letter"\n            style$="color: ;">;</div>\n        <div class="utility-panel__subtitle"\n            style$="color: ;">;</div>\n        ;\n      </div>\n    '.split(
    ";"
  );
const Qc = [
  '<div class="utility-panel__ripple"\n            data-g-category$=',
  "\n            data-g-action$=",
  '\n            data-g-label$="open ',
  '"></div>',
];
Qc.raw = [
  '<div class="utility-panel__ripple"\n            data-g-category$=',
  "\n            data-g-action$=",
  '\n            data-g-label$="open ',
  '"></div>',
];
const Rc = ["", ""];
Rc.raw = ["", ""];
const Sc = ["", ""];
Sc.raw = ["", ""];
const Tc = ['<div class="color-palette__color-weight-label">', "</div>"];
Tc.raw = ['<div class="color-palette__color-weight-label">', "</div>"];
const Uc = ['<div class="color-palette__label">', "</div>"];
Uc.raw = ['<div class="color-palette__label">', "</div>"];
const Vc = [
  '\n      <div class="color-palette__row">\n        ',
  "\n      </div>\n    ",
];
Vc.raw = [
  '\n      <div class="color-palette__row">\n        ',
  "\n      </div>\n    ",
];
const Wc =
  '\n      <div\n        class$="color-palette__cell , ,"\n        style$="background-color: ,; color: ,"\n        on-click=",">\n        <span class="color-palette__swatch-label">,</span>\n        <div class="color-palette__cell-hex-value">#,</div>\n        ,\n      </div>\n    '.split(
    ","
  );
Wc.raw =
  '\n      <div\n        class$="color-palette__cell , ,"\n        style$="background-color: ,; color: ,"\n        on-click=",">\n        <span class="color-palette__swatch-label">,</span>\n        <div class="color-palette__cell-hex-value">#,</div>\n        ,\n      </div>\n    '.split(
    ","
  );
const Xc = [
  '<div class="color-palette__ripple"\n          data-g-category$=',
  "\n          data-g-action$=",
  '\n          data-g-label="copy"></div>',
];
Xc.raw = [
  '<div class="color-palette__ripple"\n          data-g-category$=',
  "\n          data-g-action$=",
  '\n          data-g-label="copy"></div>',
];
const Yc = "900 800 700 600 500 400 300 200 100 50".split(" ");
const Zc = function (a) {
  this.app = a;
  const b = this;
  this.Cb = Ac({
    ic: "color-picker-panel",
    sb: "color-picker-panel--hide",
    Gb: "color-picker-panel--show",
    xb: function () {
      b.gb && b.gb.ma();
    },
  });
  this.gc = new cc(a);
};
x(Zc, Sb);
const $c = function (a, b, c, d) {
  const e = b ? "color-palette__cell--selected" : "";
  d = b && d ? d.charAt(0) : "";
  b = b ? (a ? Pb(a).M() : "rgba(255, 255, 255, 0.6)") : "";
  const g = Ob(a) === 0 ? "ripple-white" : "";
  return L(
    Wc,
    e,
    g,
    a.M(),
    b,
    c,
    d,
    Q(a),
    Ic(L(Xc, "inline color tool", "copy color"))
  );
};
const ad = function (a, b, c, d) {
  const e = a.map(function (e, h) {
    const g = c.some(function (a) {
      return e.ka(a);
    });
    return $c(
      e,
      g,
      function () {
        return b(a, h);
      },
      d
    );
  });
  e.reverse();
  return L(Vc, e);
};
const Z = function (a, b, c, d, e) {
  const g = [];
  g.push(L(Uc, b));
  c.reduce(function (b, c) {
    b.push(
      ad(
        c,
        function (b, c) {
          b = "#" + Q(b[c]);
          if ((c = document.querySelector("#clipboardcopy")))
            (c.value = b),
              c.select(),
              document.execCommand("copy"),
              a.app.dispatch(sc(b));
        },
        d,
        e
      )
    );
    return b;
  }, g);
  Yc.reduce(function (a, b) {
    a.push(L(Tc, b));
    return a;
  }, g);
  return g;
};
const bd = function (a) {
  const b = [];
  const c = [];
  a = w(a);
  for (let d = a.next(); !d.done; d = a.next())
    (d = lb(d.value)), b.push(d), c.push(X(d));
  return { Eb: b, yb: c };
};
const cd = function (a, b) {
  const c = [];
  c.push(Z(a, "Primary", [X(b)], [b], "PRIMARY"));
  let d = lb(rb(b).rotate(180));
  c.push(Z(a, "Complementary", [X(d)], [d]));
  d = rb(b);
  d = [d.rotate(-30), d.rotate(30)];
  d = bd(d);
  c.push(Z(a, "Analogous", d.yb, d.Eb));
  b = rb(b);
  b = [b.rotate(60), b.rotate(120)];
  b = bd(b);
  c.push(Z(a, "Triadic", b.yb, b.Eb));
  return L(Sc, c);
};
const dd = function (a, b, c) {
  c || (c = new P(1, 1, 1));
  const d = [];
  d.push(Z(a, "Primary", [X(b)], [b], "PRIMARY"));
  d.push(Z(a, "Secondary", [X(c)], [c], "SECONDARY"));
  return L(Rc, d);
};
const ed = function (a, b, c, d, e) {
  const g = e ? (Ob(e) === 0 ? "ripple-white" : "") : "";
  const h = e ? "background-color: " + e.M() + ";" : "";
  e = e ? Pb(e).M() : "rgba(255, 255, 255, 0.6)";
  return L(
    Pc,
    g,
    h,
    function () {
      a.app.dispatch({
        type: "SHOW_COLOR_PICKER",
        isPrimaryColor: d,
      });
    },
    e,
    c,
    e,
    b,
    Ic(L(Qc, "inline color tool", "color panel", d ? "primary" : "secondary"))
  );
};
const fd = function (a, b, c) {
  let d = c.secondaryColor;
  let e = S(c.primaryColor);
  let g = d && S(d);
  d =
    "/tools/color/#!/?view.left=0&view.right=0&primary.color=" +
    Q(e) +
    (g ? "&secondary.color=" + Q(g) : "");
  e = ed(a, "Primary", "P", !0, e);
  g = ed(a, "Secondary", "S", !1, g);
  const h = Rb("utility-panel");
  return L(
    Oc,
    h,
    function () {
      c.s === 0 && a.app.dispatch(tc(!b.P));
    },
    "inline color tool",
    "color panel",
    b.P ? "expand" : "expand",
    e,
    g,
    d,
    "inline color tool",
    "color panel"
  );
};
const hd = function (a, b, c, d) {
  let e = S(c.color);
  const g = b ? qc : rc;
  const h = function (b) {
    a.app.dispatch(g(b));
  };
  const k = X(e);
  const l = b ? "Primary" : "Secondary";
  c = a.gc.u(
    Object.assign({}, c, {
      L: h,
      S: function () {},
      rc: function (c) {
        a.app.dispatch(
          vc(c, b, function (a) {
            return g(tb(a));
          })
        );
      },
      sc: function (c, d, e) {
        a.app.dispatch(
          wc({ hue: c, saturation: d, b: e }, b, function (a) {
            return g(ub(a));
          })
        );
      },
    })
  );
  e = kc({
    uc: b ? "Primary" : "Secondary",
    tc: k,
    qc: function (a, b) {
      h(tb(a[b]));
    },
    selectedColor: e,
  });
  return a.Cb(L(Nc, l, e, c, gd(a, b, !d)));
};
var gd = function (a, b, c) {
  if (!b)
    return L(
      Lc,
      Ic(
        L(
          Mc,
          Wb("disabled", c ? !0 : void 0),
          "inline color tool",
          "color picker",
          b ? "primary" : "secondary",
          function () {
            a.app.dispatch({ type: "REMOVE_SECONDARY_COLOR" });
            a.app.dispatch({ type: "HIDE_COLOR_PICKER" });
          }
        ),
        function (b) {
          a.gb = b;
        }
      )
    );
};
Zc.prototype.u = function (a) {
  const b = this;
  let c = S(a.colors.primaryColor);
  let d = a.colors.secondaryColor && S(a.colors.secondaryColor);
  c = a.colors.secondaryColor ? dd(this, c, d) : cd(this, c);
  d =
    a.colors.s !== 0
      ? hd(this, a.colors.s === 1, a.colors.h, !!a.colors.secondaryColor)
      : this.Cb();
  const e = L(
    Kc,
    a.$a.ab ? "clipboard-confirmation--visible" : "",
    function () {
      b.app.dispatch(sc(""));
    }
  );
  const g = fd(this, a.Ja, a.colors);
  return L(
    Jc,
    function (c) {
      const d = c.target;
      c = c.currentTarget;
      id(d, c, "color-picker-panel") ||
        id(d, c, "utility-panel") ||
        (a.colors.s !== 0
          ? b.app.dispatch({ type: "HIDE_COLOR_PICKER" })
          : a.Ja.P && b.app.dispatch(tc(!1)));
    },
    c,
    g,
    d,
    e
  );
};
function id(a, b, c) {
  if (b.classList.contains(c)) return !0;
  for (; a && a !== b; ) {
    if (a.classList.contains(c)) return !0;
    a = a.parentElement;
  }
  return !1;
}
const jd = function (a, b) {
  Y.call(this, Zc, a, Cc, b);
};
x(jd, Y);
