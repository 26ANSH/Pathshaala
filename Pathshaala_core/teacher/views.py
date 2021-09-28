from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''<!DOCTYPE html>
<html class="js sizes customelements history pointerevents postmessage webgl websockets cssanimations csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox picture srcset webworkers" lang="zxx"><head>
<meta charset="utf-8">
<meta http-equiv="x-ua-compatible" content="ie=edge">
<title>Teacher</title>
<meta name="description" content="">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="manifest" href="site.webmanifest">
<link rel="shortcut icon" type="image/x-icon" href="assets/img/favicon.ico">

<link rel="stylesheet" href="https://preview.colorlib.com/theme/courses/assets/css/A.bootstrap.min.css+owl.carousel.min.css+slicknav.css+flaticon.css+progressbar_barfiller.css+gijgo.css+animate.min.css+animated-headline.css+magnific-popup.css+fontawesome-all.min.css+themify-icons.css+slick.css+nice-select.css,Mcc.Pxzw7oAlNi.css.pagespeed.cf.bjkLWKfzv7.css">
<link rel="stylesheet" href="https://preview.colorlib.com/theme/courses/assets/css/A.style.css.pagespeed.cf.LOwpVQvq3T.css">
</head>
<body data-new-gr-c-s-loaded="9.38.0" style="overflow: visible;">

<div id="preloader-active" style="display: none;">
<div class="preloader d-flex align-items-center justify-content-center">
<div class="preloader-inner position-relative">
<div class="preloader-circle"></div>
<div class="preloader-img pere-text">
<script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script data-pagespeed-no-defer="">//<![CDATA[
(function(){for(var g="function"==typeof Object.defineProperties?Object.defineProperty:function(b,c,a){if(a.get||a.set)throw new TypeError("ES3 does not support getters and setters.");b!=Array.prototype&&b!=Object.prototype&&(b[c]=a.value)},h="undefined"!=typeof window&&window===this?this:"undefined"!=typeof global&&null!=global?global:this,k=["String","prototype","repeat"],l=0;l<k.length-1;l++){var m=k[l];m in h||(h[m]={});h=h[m]}
var n=k[k.length-1],p=h[n],q=p?p:function(b){var c;if(null==this)throw new TypeError("The 'this' value for String.prototype.repeat must not be null or undefined");c=this+"";if(0>b||1342177279<b)throw new RangeError("Invalid count value");b|=0;for(var a="";b;)if(b&1&&(a+=c),b>>>=1)c+=c;return a};q!=p&&null!=q&&g(h,n,{configurable:!0,writable:!0,value:q});var t=this;
function u(b,c){var a=b.split("."),d=t;a[0]in d||!d.execScript||d.execScript("var "+a[0]);for(var e;a.length&&(e=a.shift());)a.length||void 0===c?d[e]?d=d[e]:d=d[e]={}:d[e]=c};function v(b){var c=b.length;if(0<c){for(var a=Array(c),d=0;d<c;d++)a[d]=b[d];return a}return[]};function w(b){var c=window;if(c.addEventListener)c.addEventListener("load",b,!1);else if(c.attachEvent)c.attachEvent("onload",b);else{var a=c.onload;c.onload=function(){b.call(this);a&&a.call(this)}}};var x;function y(b,c,a,d,e){this.h=b;this.j=c;this.l=a;this.f=e;this.g={height:window.innerHeight||document.documentElement.clientHeight||document.body.clientHeight,width:window.innerWidth||document.documentElement.clientWidth||document.body.clientWidth};this.i=d;this.b={};this.a=[];this.c={}}
function z(b,c){var a,d,e=c.getAttribute("data-pagespeed-url-hash");if(a=e&&!(e in b.c))if(0>=c.offsetWidth&&0>=c.offsetHeight)a=!1;else{d=c.getBoundingClientRect();var f=document.body;a=d.top+("pageYOffset"in window?window.pageYOffset:(document.documentElement||f.parentNode||f).scrollTop);d=d.left+("pageXOffset"in window?window.pageXOffset:(document.documentElement||f.parentNode||f).scrollLeft);f=a.toString()+","+d;b.b.hasOwnProperty(f)?a=!1:(b.b[f]=!0,a=a<=b.g.height&&d<=b.g.width)}a&&(b.a.push(e),
b.c[e]=!0)}y.prototype.checkImageForCriticality=function(b){b.getBoundingClientRect&&z(this,b)};u("pagespeed.CriticalImages.checkImageForCriticality",function(b){x.checkImageForCriticality(b)});u("pagespeed.CriticalImages.checkCriticalImages",function(){A(x)});
function A(b){b.b={};for(var c=["IMG","INPUT"],a=[],d=0;d<c.length;++d)a=a.concat(v(document.getElementsByTagName(c[d])));if(a.length&&a[0].getBoundingClientRect){for(d=0;c=a[d];++d)z(b,c);a="oh="+b.l;b.f&&(a+="&n="+b.f);if(c=!!b.a.length)for(a+="&ci="+encodeURIComponent(b.a[0]),d=1;d<b.a.length;++d){var e=","+encodeURIComponent(b.a[d]);131072>=a.length+e.length&&(a+=e)}b.i&&(e="&rd="+encodeURIComponent(JSON.stringify(B())),131072>=a.length+e.length&&(a+=e),c=!0);C=a;if(c){d=b.h;b=b.j;var f;if(window.XMLHttpRequest)f=
new XMLHttpRequest;else if(window.ActiveXObject)try{f=new ActiveXObject("Msxml2.XMLHTTP")}catch(r){try{f=new ActiveXObject("Microsoft.XMLHTTP")}catch(D){}}f&&(f.open("POST",d+(-1==d.indexOf("?")?"?":"&")+"url="+encodeURIComponent(b)),f.setRequestHeader("Content-Type","application/x-www-form-urlencoded"),f.send(a))}}}
function B(){var b={},c;c=document.getElementsByTagName("IMG");if(!c.length)return{};var a=c[0];if(!("naturalWidth"in a&&"naturalHeight"in a))return{};for(var d=0;a=c[d];++d){var e=a.getAttribute("data-pagespeed-url-hash");e&&(!(e in b)&&0<a.width&&0<a.height&&0<a.naturalWidth&&0<a.naturalHeight||e in b&&a.width>=b[e].o&&a.height>=b[e].m)&&(b[e]={rw:a.width,rh:a.height,ow:a.naturalWidth,oh:a.naturalHeight})}return b}var C="";u("pagespeed.CriticalImages.getBeaconData",function(){return C});
u("pagespeed.CriticalImages.Run",function(b,c,a,d,e,f){var r=new y(b,c,a,e,f);x=r;d&&w(function(){window.setTimeout(function(){A(r)},0)})});})();

pagespeed.CriticalImages.Run('/mod_pagespeed_beacon','https://preview.colorlib.com/theme/courses/','-ilGEe-FWC',true,false,'qYbcex8k1VI');
//]]></script><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAeCAMAAACR41cYAAAAxlBMVEUAAACAgP9VVf9mZv9ggP9gcP9aeP9ddP9ecf9YeP9acf9ccv9adf9dc/9cdf9ddf9cdP9edP9cc/9bdf9ddP9cdv9bdP9bc/9ddf9cdf9ddf9cdf9ddP9ddP9ddf9cdP9cdP9cdf9ddf9cdP9cdP9ddf9cdP9cdf9ddP9ddP9ddf9cdP9ddf9cdf9ddP9ddP9ddf9cdf9cdP9ddP9cdf9ddf9cdf9ddf9cdP9cdf9cdP9cdf9ddP9cdf9cdP9ddP9cdP9ddf+ImwOYAAAAQXRSTlMAAgMFCBARFhsgIi8wPD0/QERFRk1QXF9gZGtvcHl+f4qQn6CjqK6vsLKzv8DCxsjLz9DX2tzd3+Dl5u7v8PP6/p8evDEAAACsSURBVDjL7dNJF4EAFAXgawgpROZ5lowlCqXe//9TFnIaUMe+u7zvO293Ieikb6ajCj6S4rrz49XecTDIzarlB0xneXcPa5AXvfcW2aHl1ZrfECk8AKCk+8tz0JApAGg6FGXIBPI2RRviUaU4I0AMNZfEJOYPUws1GraxfxZgJTXij3M7yIXXnvjGRA2bx34sFtPB6bJ9w2eUOr6nbbm7OJXxM8xMAnLyIBNonzld0YLlO6pqAAAAAElFTkSuQmCC" alt="" data-pagespeed-url-hash="3114839" onload="pagespeed.CriticalImages.checkImageForCriticality(this);">
</div>
</div>
</div>
</div>

<header>

<div class="header-area header-transparent">
<div class="main-header ">
<div class="header-bottom  header-sticky">
<div class="container-fluid">
<div class="row align-items-center">

<div class="col-xl-2 col-lg-2">
<div class="logo">
  <li class="active"><a href="index.html"><h1 style="color: white;"> 📚 Paathshala </h1></a></li>
</div>
</div>
<div class="col-xl-10 col-lg-10">
<div class="menu-wrapper d-flex align-items-center justify-content-end">

<div class="main-menu d-none d-lg-block">
<nav>
<ul id="navigation">
<li><a href="/"><u style="color: white;">Return to Home</u></a></li>

<li class="button-header"><a href="/teacher" class="btn btn3">Student</a></li>
</ul>
</nav>
</div>
</div>
</div>

<div class="col-12">
<div class="mobile_menu d-block d-lg-none"><div class="slicknav_menu"><a href="#" aria-haspopup="true" role="button" tabindex="0" class="slicknav_btn slicknav_collapsed" style="outline: none;"><span class="slicknav_menutxt">MENU</span><span class="slicknav_icon"><span class="slicknav_icon-bar"></span><span class="slicknav_icon-bar"></span><span class="slicknav_icon-bar"></span></span></a><ul class="slicknav_nav slicknav_hidden" aria-hidden="true" role="menu" style="display: none;">
<li class="active"><a href="index.html" role="menuitem" tabindex="-1">Home</a></li>
<li><a href="courses.html" role="menuitem" tabindex="-1">Courses</a></li>
<li><a href="about.html" role="menuitem" tabindex="-1">About</a></li>
<li class="slicknav_collapsed slicknav_parent"><a href="#" role="menuitem" aria-haspopup="true" tabindex="-1" class="slicknav_item slicknav_row" style="outline: none;"><a href="#" tabindex="-1">Blog</a>
<span class="slicknav_arrow">+</span></a><ul class="submenu slicknav_hidden" role="menu" aria-hidden="true" style="display: none;">
<li><a href="blog.html" role="menuitem" tabindex="-1">Blog</a></li>
<li><a href="blog_details.html" role="menuitem" tabindex="-1">Blog Details</a></li>
<li><a href="elements.html" role="menuitem" tabindex="-1">Element</a></li>
</ul>
</li>
<li><a href="contact.html" role="menuitem" tabindex="-1">Contact</a></li>

<li class="button-header margin-left "><a href="#" class="btn" role="menuitem" tabindex="-1">Join</a></li>
<li class="button-header"><a href="login.html" class="btn btn3" role="menuitem" tabindex="-1">Log in</a></li>
</ul></div></div>
</div>
</div>
</div>
</div>
</div>
</div>

</header>
<main>

<section class="slider-area ">
<div class="slider-active slick-initialized slick-slider">

<div class="slick-list draggable"><div class="slick-track" style="opacity: 1; width: 1440px;"><div class="single-slider slider-height d-flex align-items-center slick-slide slick-current slick-active" data-slick-index="0" aria-hidden="false" tabindex="0" style="width: 1440px; position: relative; left: 0px; top: 0px; z-index: 999; opacity: 1;">
<div class="container">
<div class="row">
<div class="col-xl-6 col-lg-7 col-md-12">
<div class="hero__caption">
<h1 data-animation="fadeInLeft" data-delay="0.2s" class="" style="animation-delay: 0.2s;">Welcome <br> Teacher !</h1>
<p data-animation="fadeInLeft" data-delay="0.4s" class="" style="animation-delay: 0.4s;">coming up soon, Uner development</p>
<a href="#" class="btn hero-btn" data-animation="fadeInLeft" data-delay="0.7s" tabindex="0" style="animation-delay: 0.7s;">Login</a>
</div>
</div>
</div>
</div>
</div></div></div>
</div>
</section>

</div>
</div>
</div>
 ''')

# Create your views here.
