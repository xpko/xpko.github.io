# 为Jekyll添加评论系统

目前使用的是：https://giscus.app

直接按官方文档提示操作即可

## 自定义client.js

原始js：https://giscus.app/client.js

```js
(function(){function h(a){return'[giscus] An error occurred. Error message: "'.concat(a,'".')}function l(a,g){void 0===g&&(g=!1);g=g?"meta[property='og:".concat(a,"'],"):"";return(a=document.querySelector(g+"meta[name='".concat(a,"']")))?a.content:""}function p(){delete c.session;var a="".concat(k,"/widget?").concat(new URLSearchParams(c));e.src=a}var m=document.currentScript,k=(new URL(m.src)).origin,b=new URL(location.href),d=b.searchParams.get("giscus")||"",n=localStorage.getItem("giscus-session");
b.searchParams.delete("giscus");b.hash="";var f=b.toString();if(d)localStorage.setItem("giscus-session",JSON.stringify(d)),history.replaceState(void 0,document.title,f);else if(n)try{d=JSON.parse(n)}catch(a){localStorage.removeItem("giscus-session"),console.warn("".concat(h(null===a||void 0===a?void 0:a.message)," Session has been cleared."))}b=m.dataset;var c={};c.origin=f;c.session=d;c.theme=b.theme;c.reactionsEnabled=b.reactionsEnabled||"1";c.emitMetadata=b.emitMetadata||"0";c.inputPosition=b.inputPosition||
"bottom";c.repo=b.repo;c.repoId=b.repoId;c.category=b.category||"";c.categoryId=b.categoryId;c.strict=b.strict||"0";c.description=l("description",!0);c.backLink=l("giscus:backlink")||f;switch(b.mapping){case "url":c.term=f;break;case "title":c.term=document.title;break;case "og:title":c.term=l("title",!0);break;case "specific":c.term=b.term;break;case "number":c.number=b.term;break;default:c.term=2>location.pathname.length?"index":location.pathname.substring(1).replace(/\.\w+$/,"")}var q=(d=document.querySelector(".giscus"))&&
d.id;q&&(c.origin="".concat(f,"#").concat(q));f=b.lang?"/".concat(b.lang):"";f="".concat(k).concat(f,"/widget?").concat(new URLSearchParams(c));b="lazy"===b.loading?"lazy":void 0;var e=document.createElement("iframe");Object.entries({class:"giscus-frame giscus-frame--loading",title:"Comments",scrolling:"no",allow:"clipboard-write",src:f,loading:b}).forEach(function(a){var g=a[0];return(a=a[1])&&e.setAttribute(g,a)});e.style.opacity="0";e.addEventListener("load",function(){e.style.removeProperty("opacity");
e.classList.remove("giscus-frame--loading")});b=document.getElementById("giscus-css")||document.createElement("link");b.id="giscus-css";b.rel="stylesheet";b.href="".concat(k,"/default.css");document.head.prepend(b);if(d){for(;d.firstChild;)d.firstChild.remove();d.appendChild(e)}else d=document.createElement("div"),d.setAttribute("class","giscus"),d.appendChild(e),m.insertAdjacentElement("afterend",d);window.addEventListener("message",function(a){a.origin===k&&(a=a.data,"object"===typeof a&&a.giscus&&
(a.giscus.resizeHeight&&(e.style.height="".concat(a.giscus.resizeHeight,"px")),a.giscus.signOut?(localStorage.removeItem("giscus-session"),console.log("[giscus] User has logged out. Session has been cleared."),p()):a.giscus.error&&(a=a.giscus.error,a.includes("Bad credentials")||a.includes("Invalid state value")||a.includes("State has expired")?null!==localStorage.getItem("giscus-session")?(localStorage.removeItem("giscus-session"),console.warn("".concat(h(a)," Session has been cleared.")),p()):n||
console.error("".concat(h(a)," No session is stored initially. ").concat("Please consider reporting this error at https://github.com/giscus/giscus/issues/new.")):a.includes("Discussion not found")?console.warn("[giscus] ".concat(a,". A new discussion will be created if a comment/reaction is submitted.")):a.includes("API rate limit exceeded")?console.warn(h(a)):console.error("".concat(h(a)," ").concat("Please consider reporting this error at https://github.com/giscus/giscus/issues/new.")))))})})();
```

补丁：支持url解码，否则评论里标题不显示中文

![image-20241223151219375](./为Jekyll添加评论系统/image-20241223151219375.png)

![image-20241223151447138](./为Jekyll添加评论系统/image-20241223151447138.png)

补丁：去掉描述，优化web 链接显示

![image-20241223152556536](./为Jekyll添加评论系统/image-20241223152556536.png)

![image-20241223152611939](./为Jekyll添加评论系统/image-20241223152611939.png)

