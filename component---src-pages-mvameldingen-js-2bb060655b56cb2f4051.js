/*! For license information please see component---src-pages-mvameldingen-js-2bb060655b56cb2f4051.js.LICENSE.txt */
(window.webpackJsonp=window.webpackJsonp||[]).push([[11],{"5toE":function(e,t,n){"use strict";function r(e){return(r="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var o,l=function(e){if(e&&e.__esModule)return e;if(null===e||"object"!==r(e)&&"function"!=typeof e)return{default:e};var t=a();if(t&&t.has(e))return t.get(e);var n={},o=Object.defineProperty&&Object.getOwnPropertyDescriptor;for(var l in e)if(Object.prototype.hasOwnProperty.call(e,l)){var i=o?Object.getOwnPropertyDescriptor(e,l):null;i&&(i.get||i.set)?Object.defineProperty(n,l,i):n[l]=e[l]}n.default=e,t&&t.set(e,n);return n}(n("q1tI")),i=(o=n("2qmW"))&&o.__esModule?o:{default:o};function a(){if("function"!=typeof WeakMap)return null;var e=new WeakMap;return a=function(){return e},e}function u(){return(u=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e}).apply(this,arguments)}function c(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},l=Object.keys(e);for(r=0;r<l.length;r++)n=l[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(r=0;r<l.length;r++)n=l[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var s=function(e){return l.createElement(l.Fragment,null,l.createElement(i.default,{iconName:e.icon}),l.isValidElement(e.heading)?e.heading:l.createElement((function(){switch(e.headingLevel){case 3:return l.createElement("h3",null,e.heading);case 4:return l.createElement("h4",null,e.heading);case 5:return l.createElement("h5",null,e.heading);case 6:return l.createElement("h6",null,e.heading);default:return l.createElement("h2",null,e.heading)}}),null),l.createElement("p",null,e.description||e.children))},f=function(e){var t=e.renderContent,n=e.id,r=e.className,o=e.icon,i=e.heading,a=e.description,f=e.children,p=e.useButtons,d=e.headingLevel,y=c(e,["renderContent","id","className","icon","heading","description","children","useButtons","headingLevel"]),m={icon:o,heading:i,description:a,children:f,headingLevel:d};if("function"==typeof e.to){if(p)return l.createElement("button",{onClick:e.to},l.createElement(s,m));throw new Error('When property "to" is set as function you have to set "useButtons" to true')}return l.createElement("li",{id:n,key:e.to,className:r},t?t(e.to,l.createElement(s,m)):l.createElement("a",u({href:e.to},y),l.createElement(s,m)))};t.default=f},"8fPi":function(e,t,n){"use strict";function r(e){return(r="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var o=c(n("TSYQ")),l=function(e){if(e&&e.__esModule)return e;if(null===e||"object"!==r(e)&&"function"!=typeof e)return{default:e};var t=u();if(t&&t.has(e))return t.get(e);var n={},o=Object.defineProperty&&Object.getOwnPropertyDescriptor;for(var l in e)if(Object.prototype.hasOwnProperty.call(e,l)){var i=o?Object.getOwnPropertyDescriptor(e,l):null;i&&(i.get||i.set)?Object.defineProperty(n,l,i):n[l]=e[l]}n.default=e,t&&t.set(e,n);return n}(n("q1tI")),i=c(n("5toE")),a=n("A9dO");function u(){if("function"!=typeof WeakMap)return null;var e=new WeakMap;return u=function(){return e},e}function c(e){return e&&e.__esModule?e:{default:e}}function s(){return(s=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e}).apply(this,arguments)}function f(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},l=Object.keys(e);for(r=0;r<l.length;r++)n=l[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(r=0;r<l.length;r++)n=l[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var p=function(e){var t=e.children,n=e.contents,r=e.className,u=(e.type,e.alignIcon,e.alignTitle,e.alignDescription,e.ariaLabel),c=e.headingLevel,p=e.useButtons,d=f(e,["children","contents","className","type","alignIcon","alignTitle","alignDescription","ariaLabel","headingLevel","useButtons"]),y=(0,a.getClassNames)(e);return l.createElement("nav",s({"aria-label":u},d,{className:(0,o.default)(y.nav,(0,a.getClassNames)(e),r)}),l.createElement("ul",null,n&&n.map((function(e,t){var n=s({},e);return l.createElement(i.default,s({key:t+"."+n.to,className:y.content,headingLevel:c,useButtons:p},n))})),l.Children.map(t,(function(e,t){if(l.isValidElement(e))return l.createElement(i.default,s({key:t+"."+e.props.to,className:y.content,headingLevel:c,useButtons:p},e.props),e.props.children)}))))};p.defaultProps={alignDescription:"center",alignIcon:"center",alignTitle:"center",type:"center"};var d=p;t.default=d},A9dO:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.getClassNames=void 0;var r=n("65oB"),o=n("tqYG");function l(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?l(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):l(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function u(e){if("left"===e.type)return{display:"block"}}function c(e){return"right"===e.alignIcon?{fontSize:"28px",float:"right"}:{fontSize:"42px",display:"inherit",margin:"16px 0",textAlign:"center",color:"black"}}function s(e){var t=(0,o.getTheme)().palette;if("left"===e.alignTitle)return{textAlign:"left",margin:0,marginBottom:"8px",color:t.skeColor.blue}}function f(e){var t=(0,o.getTheme)().palette;if("left"===e.alignDescription)return{margin:0,textAlign:"left",lineHeight:"25px",color:t.skeColor.blackAlt}}t.getClassNames=function(e){var t=(0,o.getTheme)().palette;return(0,r.mergeStyleSets)({content:{selectors:{"& i":i({},c(e)),"& p":i({margin:0,textAlign:"center",lineHeight:"25px",color:t.skeColor.blackAlt},f(e)),"& h2, h3, h4, h5, h6":i({textAlign:"center",margin:0,marginBottom:"8px",color:t.skeColor.blue},s(e)),"&:active, &:focus, &:hover":{selectors:{h2:{color:t.skeColor.darkBlue}}}}},nav:{selectors:{"& a, & button":{border:"0",margin:"auto"},"& button":i({backgroundColor:"inherit"},s(e)),"& ul":i({display:"flex",flexWrap:"wrap",padding:0,justifyContent:"space-between"},u(e)),"& ul li":{borderBottom:"3px solid ".concat(t.skeColor.darkBlue),position:"relative",textDecoration:"none",listStyle:"none",display:"flex",marginBottom:"32px",flexBasis:"46%"},"& ul li > a, & ul li > button":{color:t.skeColor.darkBlue,textDecoration:"none",paddingBottom:"16px",paddingLeft:"16px",paddingRight:"16px",margin:"0 !important",width:"100%",transition:"all 0.2s ease"},"& ul li > a:active, & ul li > a:focus, & ul li > a:hover, & ul li > button:active, & ul li > button:focus, & ul li > button:hover":{backgroundColor:t.skeColor.lightBlue,outline:"none",transition:"background-color .2s"},"& ul li > a::after, & ul li > button::after":{content:'""',position:"absolute",display:"inline-block",left:0,bottom:0,backgroundColor:t.skeColor.darkBlue,transition:"height 0.1s",width:"100%",height:0},"& ul li > a:focus:after, & ul li > a:hover:after, & ul li > button:focus:after, & ul li > button:hover:after":{height:2},"@media (max-width: 1023px)":{selectors:{"ul li":{flexBasis:"100%"}}}}}})}},TSYQ:function(e,t,n){var r;!function(){"use strict";var n={}.hasOwnProperty;function o(){for(var e=[],t=0;t<arguments.length;t++){var r=arguments[t];if(r){var l=typeof r;if("string"===l||"number"===l)e.push(r);else if(Array.isArray(r)&&r.length){var i=o.apply(null,r);i&&e.push(i)}else if("object"===l)for(var a in r)n.call(r,a)&&r[a]&&e.push(a)}}return e.join(" ")}e.exports?(o.default=o,e.exports=o):void 0===(r=function(){return o}.apply(t,[]))||(e.exports=r)}()},okai:function(e,t,n){"use strict";function r(e){return(r="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}Object.defineProperty(t,"__esModule",{value:!0});var o={};Object.defineProperty(t,"default",{enumerable:!0,get:function(){return l.default}});var l=function(e){if(e&&e.__esModule)return e;if(null===e||"object"!==r(e)&&"function"!=typeof e)return{default:e};var t=i();if(t&&t.has(e))return t.get(e);var n={},o=Object.defineProperty&&Object.getOwnPropertyDescriptor;for(var l in e)if(Object.prototype.hasOwnProperty.call(e,l)){var a=o?Object.getOwnPropertyDescriptor(e,l):null;a&&(a.get||a.set)?Object.defineProperty(n,l,a):n[l]=e[l]}n.default=e,t&&t.set(e,n);return n}(n("8fPi"));function i(){if("function"!=typeof WeakMap)return null;var e=new WeakMap;return i=function(){return e},e}Object.keys(l).forEach((function(e){"default"!==e&&"__esModule"!==e&&(Object.prototype.hasOwnProperty.call(o,e)||Object.defineProperty(t,e,{enumerable:!0,get:function(){return l[e]}}))}))},q0Vb:function(e,t,n){"use strict";n.d(t,"a",(function(){return c}));var r=n("q1tI"),o=n.n(r),l=n("1cZw"),i=n.n(l);const a={sm:10,smPush:1,md:10,mdPush:1,lg:10,lgPush:1,xl:3,xlPush:3,xxl:3,xxlPush:3},u={...a,xl:6,xlPush:3,xxl:6,xxlPush:3},c=e=>{let{children:t}=e;return o.a.createElement(i.a.Row,null,o.a.createElement(i.a.Col,u,t))}},x71T:function(e,t,n){"use strict";n.r(t);var r=n("q1tI"),o=n.n(r),l=n("1cZw"),i=n.n(l),a=n("okai"),u=n.n(a),c=n("vBTi"),s=n.n(c),f=n("q0Vb"),p=n("Wbzz");t.default=e=>{let{data:{allMarkdownRemark:{edges:t},site:{pathPrefix:n}}}=e;const r=n,l=t.filter(e=>{let{node:t}=e;return t.fields&&t.fields.slug.search("/mvameldingen/")>=0}).map(e=>{let{node:t}=e;return{to:""+r+t.fields.slug,icon:t.frontmatter.icon,heading:t.frontmatter.title,description:t.frontmatter.description||""}});return o.a.createElement(s.a,null,o.a.createElement(i.a,null,o.a.createElement(f.a,null,o.a.createElement("a",{href:"https://skatteetaten.github.io/mva-meldingen/mvameldingen_eng/"},"English"),o.a.createElement("h1",null,"Dokumentasjon mva-meldingen")),o.a.createElement(f.a,null,o.a.createElement(u.a,{contents:l,renderContent:(e,t)=>o.a.createElement(p.a,{to:e},t)}))))}}}]);
//# sourceMappingURL=component---src-pages-mvameldingen-js-2bb060655b56cb2f4051.js.map