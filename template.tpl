<!doctype html>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<html>
<head>

<style type="text/css">

/* --------------------------------------------------------------
Taken from blueprint css framework
-------------------------------------------------------------- */
html { font-size:100.01%; }
body {
  font-size: 75%;
  color: #222;
  background: #fff;
  font-family: "Helvetica Neue", Arial, Helvetica, sans-serif;
}
h1,h2,h3,h4,h5,h6 { font-weight: normal; color: #111; }
h1 { font-size: 3em; line-height: 1; margin-bottom: 0.5em; }
h2 { font-size: 2em; margin-bottom: 0.75em; }
h3 { font-size: 1.5em; line-height: 1; margin-bottom: 1em; }
h4 { font-size: 1.2em; line-height: 1.25; margin-bottom: 1.25em; }
h5 { font-size: 1em; font-weight: bold; margin-bottom: 1.5em; }
h6 { font-size: 1em; font-weight: bold; }
h1 img, h2 img, h3 img,
h4 img, h5 img, h6 img {
  margin: 0;
}

p           { margin: 0 0 1.5em; }

a:focus,
a:hover     { color: #09f; }
a           { color: #06c; text-decoration: underline; }

blockquote  { margin: 1.5em; color: #666; font-style: italic; }
strong,dfn	{ font-weight: bold; }
em,dfn      { font-style: italic; }
sup, sub    { line-height: 0; }
abbr,
acronym     { border-bottom: 1px dotted #666; }
address     { margin: 0 0 1.5em; font-style: italic; }
del         { color:#666; }
pre         { margin: 1.5em 0; white-space: pre; }
pre,code,tt { font: 1em 'andale mono', 'lucida console', monospace; line-height: 1.5; }

li ul,
li ol       { margin: 0; }
ul, ol      { margin: 0 1.5em 1.5em 0; padding-left: 1.5em; }

ul          { list-style-type: disc; }
ol          { list-style-type: decimal; }

dl          { margin: 0 0 1.5em 0; }
dl dt       { font-weight: bold; }
dd          { margin-left: 1.5em;}

table       { margin-bottom: 1.4em; width:100%; }
th          { font-weight: bold; }
thead th    { background: #c3d9ff; }
th,td,caption { padding: 4px 10px 4px 5px; }
tbody tr:nth-child(even) td, 
tbody tr.even td  { 
	background: #e5ecf9; 
}
tfoot       { font-style: italic; }
caption     { background: #eee; }

div.content {
width:60%; 
margin:0 auto;
/* border: 1px solid #ccc; */
}

</style>
</head>
<body>
  <div class="content">
    $markdown_content
  </div>
</<body>
</html>