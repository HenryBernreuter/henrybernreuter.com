<html>
<head><meta charset="utf-8" />

<title>titanic-solution</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">

/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  }
  div.output_wrapper {
    display: block;
    page-break-inside: avoid;
  }
  div.output {
    display: block;
    page-break-inside: avoid;
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Titanic:-Machine-Learning-from-Disaster">Titanic: Machine Learning from Disaster<a class="anchor-link" href="#Titanic:-Machine-Learning-from-Disaster">&#182;</a></h1><h3 id="Predict-survival-on-the-Titanic">Predict survival on the Titanic<a class="anchor-link" href="#Predict-survival-on-the-Titanic">&#182;</a></h3><ul>
<li>Defining the problem statement</li>
<li>Collecting the data</li>
<li>Exploratory data analysis</li>
<li>Feature engineering</li>
<li>Modelling</li>
<li>Testing</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="1.-Defining-the-problem-statement">1. Defining the problem statement<a class="anchor-link" href="#1.-Defining-the-problem-statement">&#182;</a></h2><p>Complete the analysis of what sorts of people were likely to survive.<br>
In particular, we ask you to apply the tools of machine learning to predict which passengers survived the Titanic tragedy.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="2.-Collecting-the-data">2. Collecting the data<a class="anchor-link" href="#2.-Collecting-the-data">&#182;</a></h2><p>Download from kaggle directly <a href="https://www.kaggle.com/c/titanic/data">kaggle</a></p>
<h3 id="load-train,-test-dataset-using-Pandas">load train, test dataset using Pandas<a class="anchor-link" href="#load-train,-test-dataset-using-Pandas">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>

<span class="n">train</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;input/train.csv&#39;</span><span class="p">)</span>
<span class="n">test</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;input/test.csv&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="3.-Exploratory-data-analysis">3. Exploratory data analysis<a class="anchor-link" href="#3.-Exploratory-data-analysis">&#182;</a></h2><p>Printing first 5 rows of the train dataset.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[3]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Data-Dictionary">Data Dictionary<a class="anchor-link" href="#Data-Dictionary">&#182;</a></h3><ul>
<li>Survived:     0 = No, 1 = Yes  </li>
<li>pclass:   Ticket class    1 = 1st, 2 = 2nd, 3 = 3rd   </li>
<li>sibsp:    # of siblings / spouses aboard the Titanic      </li>
<li>parch:    # of parents / children aboard the Titanic      </li>
<li>ticket:   Ticket number   </li>
<li>cabin:    Cabin number    </li>
<li>embarked: Port of Embarkation C = Cherbourg, Q = Queenstown, S = Southampton  </li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>Total rows and columns</strong></p>
<p>We can see that there are 891 rows and 12 columns in our training dataset.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">test</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[4]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>892</td>
      <td>3</td>
      <td>Kelly, Mr. James</td>
      <td>male</td>
      <td>34.5</td>
      <td>0</td>
      <td>0</td>
      <td>330911</td>
      <td>7.8292</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>1</th>
      <td>893</td>
      <td>3</td>
      <td>Wilkes, Mrs. James (Ellen Needs)</td>
      <td>female</td>
      <td>47.0</td>
      <td>1</td>
      <td>0</td>
      <td>363272</td>
      <td>7.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>2</th>
      <td>894</td>
      <td>2</td>
      <td>Myles, Mr. Thomas Francis</td>
      <td>male</td>
      <td>62.0</td>
      <td>0</td>
      <td>0</td>
      <td>240276</td>
      <td>9.6875</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>3</th>
      <td>895</td>
      <td>3</td>
      <td>Wirz, Mr. Albert</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>315154</td>
      <td>8.6625</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>896</td>
      <td>3</td>
      <td>Hirvonen, Mrs. Alexander (Helga E Lindqvist)</td>
      <td>female</td>
      <td>22.0</td>
      <td>1</td>
      <td>1</td>
      <td>3101298</td>
      <td>12.2875</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">shape</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[5]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(891, 12)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">test</span><span class="o">.</span><span class="n">shape</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[6]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(418, 11)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
PassengerId    891 non-null int64
Survived       891 non-null int64
Pclass         891 non-null int64
Name           891 non-null object
Sex            891 non-null object
Age            714 non-null float64
SibSp          891 non-null int64
Parch          891 non-null int64
Ticket         891 non-null object
Fare           891 non-null float64
Cabin          204 non-null object
Embarked       889 non-null object
dtypes: float64(2), int64(5), object(5)
memory usage: 66.2+ KB
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">test</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 418 entries, 0 to 417
Data columns (total 11 columns):
PassengerId    418 non-null int64
Pclass         418 non-null int64
Name           418 non-null object
Sex            418 non-null object
Age            332 non-null float64
SibSp          418 non-null int64
Parch          418 non-null int64
Ticket         418 non-null object
Fare           417 non-null float64
Cabin          91 non-null object
Embarked       418 non-null object
dtypes: float64(2), int64(4), object(5)
memory usage: 36.0+ KB
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><em>Age</em> value is missing for many rows.</p>
<p>Out of 891 rows, the <em>Age</em> value is present only in 714 rows.</p>
<p>Similarly, <em>Cabin</em> values are also missing in many rows. Only 204 out of 891 rows have <em>Cabin</em> values.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">isnull</span><span class="p">()</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[5]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">test</span><span class="o">.</span><span class="n">isnull</span><span class="p">()</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[6]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>PassengerId      0
Pclass           0
Name             0
Sex              0
Age             86
SibSp            0
Parch            0
Ticket           0
Fare             1
Cabin          327
Embarked         0
dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>There are 177 rows with missing <em>Age</em>, 687 rows with missing <em>Cabin</em> and 2 rows with missing <em>Embarked</em> information.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="import-python-lib-for-visualization">import python lib for visualization<a class="anchor-link" href="#import-python-lib-for-visualization">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="o">%</span><span class="k">matplotlib</span> inline
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>
<span class="n">sns</span><span class="o">.</span><span class="n">set</span><span class="p">()</span> <span class="c1"># setting seaborn default for plots</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Bar-Chart-for-Categorical-Features">Bar Chart for Categorical Features<a class="anchor-link" href="#Bar-Chart-for-Categorical-Features">&#182;</a></h3><ul>
<li>Pclass</li>
<li>Sex</li>
<li>SibSp ( # of siblings and spouse)</li>
<li>Parch ( # of parents and children)</li>
<li>Embarked</li>
<li>Cabin</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">bar_chart</span><span class="p">(</span><span class="n">feature</span><span class="p">):</span>
    <span class="n">survived</span> <span class="o">=</span> <span class="n">train</span><span class="p">[</span><span class="n">train</span><span class="p">[</span><span class="s1">&#39;Survived&#39;</span><span class="p">]</span><span class="o">==</span><span class="mi">1</span><span class="p">][</span><span class="n">feature</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
    <span class="n">dead</span> <span class="o">=</span> <span class="n">train</span><span class="p">[</span><span class="n">train</span><span class="p">[</span><span class="s1">&#39;Survived&#39;</span><span class="p">]</span><span class="o">==</span><span class="mi">0</span><span class="p">][</span><span class="n">feature</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">([</span><span class="n">survived</span><span class="p">,</span><span class="n">dead</span><span class="p">])</span>
    <span class="n">df</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Survived&#39;</span><span class="p">,</span><span class="s1">&#39;Dead&#39;</span><span class="p">]</span>
    <span class="n">df</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">&#39;bar&#39;</span><span class="p">,</span><span class="n">stacked</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">5</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">bar_chart</span><span class="p">(</span><span class="s1">&#39;Sex&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The Chart confirms <strong>Women</strong> more likely survivied than <strong>Men</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">bar_chart</span><span class="p">(</span><span class="s1">&#39;Pclass&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The Chart confirms <strong>1st class</strong> more likely survivied than <strong>other classes</strong><br>
The Chart confirms <strong>3rd class</strong> more likely dead than <strong>other classes</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">bar_chart</span><span class="p">(</span><span class="s1">&#39;SibSp&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The Chart confirms <strong>a person aboarded with more than 2 siblings or spouse</strong> more likely survived<br>
The Chart confirms <strong> a person aboarded without siblings or spouse</strong> more likely dead</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">bar_chart</span><span class="p">(</span><span class="s1">&#39;Parch&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The Chart confirms <strong>a person aboarded with more than 2 parents or children</strong> more likely survived<br>
The Chart confirms <strong> a person aboarded alone</strong> more likely dead</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">bar_chart</span><span class="p">(</span><span class="s1">&#39;Embarked&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The Chart confirms <strong>a person aboarded from C</strong> slightly more likely survived<br>
The Chart confirms <strong>a person aboarded from Q</strong> more likely dead<br>
The Chart confirms <strong>a person aboarded from S</strong> more likely dead</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="4.-Feature-engineering">4. Feature engineering<a class="anchor-link" href="#4.-Feature-engineering">&#182;</a></h2><p>Feature engineering is the process of using domain knowledge of the data<br>
to create features (<strong>feature vectors</strong>) that make machine learning algorithms work.</p>
<p>feature vector is an n-dimensional vector of numerical features that represent some object.<br>
Many algorithms in machine learning require a numerical representation of objects,<br>
since such representations facilitate processing and statistical analysis.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[14]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="4.1-how-titanic-sank?">4.1 how titanic sank?<a class="anchor-link" href="#4.1-how-titanic-sank?">&#182;</a></h3><p>sank from the bow of the ship where third class rooms located<br>
conclusion, Pclass is key feature for classifier</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[15]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>0</td>
      <td>3</td>
      <td>Moran, Mr. James</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>330877</td>
      <td>8.4583</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>McCarthy, Mr. Timothy J</td>
      <td>male</td>
      <td>54.0</td>
      <td>0</td>
      <td>0</td>
      <td>17463</td>
      <td>51.8625</td>
      <td>E46</td>
      <td>S</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>0</td>
      <td>3</td>
      <td>Palsson, Master. Gosta Leonard</td>
      <td>male</td>
      <td>2.0</td>
      <td>3</td>
      <td>1</td>
      <td>349909</td>
      <td>21.0750</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)</td>
      <td>female</td>
      <td>27.0</td>
      <td>0</td>
      <td>2</td>
      <td>347742</td>
      <td>11.1333</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>1</td>
      <td>2</td>
      <td>Nasser, Mrs. Nicholas (Adele Achem)</td>
      <td>female</td>
      <td>14.0</td>
      <td>1</td>
      <td>0</td>
      <td>237736</td>
      <td>30.0708</td>
      <td>NaN</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="4.2-Name">4.2 Name<a class="anchor-link" href="#4.2-Name">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train_test_data</span> <span class="o">=</span> <span class="p">[</span><span class="n">train</span><span class="p">,</span> <span class="n">test</span><span class="p">]</span> <span class="c1"># combining train and test dataset</span>

<span class="k">for</span> <span class="n">dataset</span> <span class="ow">in</span> <span class="n">train_test_data</span><span class="p">:</span>
    <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Title&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Name&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">extract</span><span class="p">(</span><span class="s1">&#39; ([A-Za-z]+)\.&#39;</span><span class="p">,</span> <span class="n">expand</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="p">[</span><span class="s1">&#39;Title&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[17]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Mr          517
Miss        182
Mrs         125
Master       40
Dr            7
Rev           6
Col           2
Major         2
Mlle          2
Don           1
Capt          1
Mme           1
Lady          1
Ms            1
Sir           1
Jonkheer      1
Countess      1
Name: Title, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">test</span><span class="p">[</span><span class="s1">&#39;Title&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[18]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Mr        240
Miss       78
Mrs        72
Master     21
Col         2
Rev         2
Dona        1
Ms          1
Dr          1
Name: Title, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Title-map">Title map<a class="anchor-link" href="#Title-map">&#182;</a></h4><p>Mr : 0<br>
Miss : 1<br>
Mrs: 2<br>
Others: 3</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">title_mapping</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;Mr&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s2">&quot;Miss&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s2">&quot;Mrs&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
                 <span class="s2">&quot;Master&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;Dr&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;Rev&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;Col&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;Major&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;Mlle&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span><span class="s2">&quot;Countess&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span>
                 <span class="s2">&quot;Ms&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;Lady&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;Jonkheer&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;Don&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;Dona&quot;</span> <span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;Mme&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span><span class="s2">&quot;Capt&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span><span class="s2">&quot;Sir&quot;</span><span class="p">:</span> <span class="mi">3</span> <span class="p">}</span>
<span class="k">for</span> <span class="n">dataset</span> <span class="ow">in</span> <span class="n">train_test_data</span><span class="p">:</span>
    <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Title&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Title&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">title_mapping</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[20]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">test</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[21]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>892</td>
      <td>3</td>
      <td>Kelly, Mr. James</td>
      <td>male</td>
      <td>34.5</td>
      <td>0</td>
      <td>0</td>
      <td>330911</td>
      <td>7.8292</td>
      <td>NaN</td>
      <td>Q</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>893</td>
      <td>3</td>
      <td>Wilkes, Mrs. James (Ellen Needs)</td>
      <td>female</td>
      <td>47.0</td>
      <td>1</td>
      <td>0</td>
      <td>363272</td>
      <td>7.0000</td>
      <td>NaN</td>
      <td>S</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>894</td>
      <td>2</td>
      <td>Myles, Mr. Thomas Francis</td>
      <td>male</td>
      <td>62.0</td>
      <td>0</td>
      <td>0</td>
      <td>240276</td>
      <td>9.6875</td>
      <td>NaN</td>
      <td>Q</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>895</td>
      <td>3</td>
      <td>Wirz, Mr. Albert</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>315154</td>
      <td>8.6625</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>896</td>
      <td>3</td>
      <td>Hirvonen, Mrs. Alexander (Helga E Lindqvist)</td>
      <td>female</td>
      <td>22.0</td>
      <td>1</td>
      <td>1</td>
      <td>3101298</td>
      <td>12.2875</td>
      <td>NaN</td>
      <td>S</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">bar_chart</span><span class="p">(</span><span class="s1">&#39;Title&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># delete unnecessary feature from dataset</span>
<span class="n">train</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s1">&#39;Name&#39;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">test</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s1">&#39;Name&#39;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[24]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">test</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[25]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>892</td>
      <td>3</td>
      <td>male</td>
      <td>34.5</td>
      <td>0</td>
      <td>0</td>
      <td>330911</td>
      <td>7.8292</td>
      <td>NaN</td>
      <td>Q</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>893</td>
      <td>3</td>
      <td>female</td>
      <td>47.0</td>
      <td>1</td>
      <td>0</td>
      <td>363272</td>
      <td>7.0000</td>
      <td>NaN</td>
      <td>S</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>894</td>
      <td>2</td>
      <td>male</td>
      <td>62.0</td>
      <td>0</td>
      <td>0</td>
      <td>240276</td>
      <td>9.6875</td>
      <td>NaN</td>
      <td>Q</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>895</td>
      <td>3</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>315154</td>
      <td>8.6625</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>896</td>
      <td>3</td>
      <td>female</td>
      <td>22.0</td>
      <td>1</td>
      <td>1</td>
      <td>3101298</td>
      <td>12.2875</td>
      <td>NaN</td>
      <td>S</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="4.3-Sex">4.3 Sex<a class="anchor-link" href="#4.3-Sex">&#182;</a></h3><p>male: 0
female: 1</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sex_mapping</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;male&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s2">&quot;female&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">}</span>
<span class="k">for</span> <span class="n">dataset</span> <span class="ow">in</span> <span class="n">train_test_data</span><span class="p">:</span>
    <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Sex&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Sex&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">sex_mapping</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">bar_chart</span><span class="p">(</span><span class="s1">&#39;Sex&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="4.4-Age">4.4 Age<a class="anchor-link" href="#4.4-Age">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="4.4.1-some-age-is-missing">4.4.1 some age is missing<a class="anchor-link" href="#4.4.1-some-age-is-missing">&#182;</a></h4><p>Let's use Title's median age for missing Age</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[29]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>330877</td>
      <td>8.4583</td>
      <td>NaN</td>
      <td>Q</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>54.0</td>
      <td>0</td>
      <td>0</td>
      <td>17463</td>
      <td>51.8625</td>
      <td>E46</td>
      <td>S</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2.0</td>
      <td>3</td>
      <td>1</td>
      <td>349909</td>
      <td>21.0750</td>
      <td>NaN</td>
      <td>S</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>27.0</td>
      <td>0</td>
      <td>2</td>
      <td>347742</td>
      <td>11.1333</td>
      <td>NaN</td>
      <td>S</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>14.0</td>
      <td>1</td>
      <td>0</td>
      <td>237736</td>
      <td>30.0708</td>
      <td>NaN</td>
      <td>C</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># fill missing age with median age for each title (Mr, Mrs, Miss, Others)</span>
<span class="n">train</span><span class="p">[</span><span class="s2">&quot;Age&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">train</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">&quot;Title&quot;</span><span class="p">)[</span><span class="s2">&quot;Age&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="s2">&quot;median&quot;</span><span class="p">),</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">test</span><span class="p">[</span><span class="s2">&quot;Age&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">&quot;Title&quot;</span><span class="p">)[</span><span class="s2">&quot;Age&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="s2">&quot;median&quot;</span><span class="p">),</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[33]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">30</span><span class="p">)</span>
<span class="n">train</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">&quot;Title&quot;</span><span class="p">)[</span><span class="s2">&quot;Age&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="s2">&quot;median&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[33]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>0      30.0
1      35.0
2      21.0
3      35.0
4      30.0
5      30.0
6      30.0
7       9.0
8      35.0
9      35.0
10     21.0
11     21.0
12     30.0
13     30.0
14     21.0
15     35.0
16      9.0
17     30.0
18     35.0
19     35.0
20     30.0
21     30.0
22     21.0
23     30.0
24     21.0
25     35.0
26     30.0
27     30.0
28     21.0
29     30.0
       ...
861    30.0
862    35.0
863    21.0
864    30.0
865    35.0
866    21.0
867    30.0
868    30.0
869     9.0
870    30.0
871    35.0
872    30.0
873    30.0
874    35.0
875    21.0
876    30.0
877    30.0
878    30.0
879    35.0
880    35.0
881    30.0
882    21.0
883    30.0
884    30.0
885    35.0
886     9.0
887    21.0
888    21.0
889    30.0
890    30.0
Name: Age, Length: 891, dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[34]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">facet</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">FacetGrid</span><span class="p">(</span><span class="n">train</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s2">&quot;Survived&quot;</span><span class="p">,</span><span class="n">aspect</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">,</span><span class="s1">&#39;Age&#39;</span><span class="p">,</span><span class="n">shade</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">xlim</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()))</span>
<span class="n">facet</span><span class="o">.</span><span class="n">add_legend</span><span class="p">()</span>

<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">facet</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">FacetGrid</span><span class="p">(</span><span class="n">train</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s2">&quot;Survived&quot;</span><span class="p">,</span><span class="n">aspect</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">,</span><span class="s1">&#39;Age&#39;</span><span class="p">,</span><span class="n">shade</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">xlim</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()))</span>
<span class="n">facet</span><span class="o">.</span><span class="n">add_legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlim</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">20</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[35]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(0, 20)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA4wAAADQCAYAAABMbu+zAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvnQurowAAIABJREFUeJzt3XmUJNdB5/tvRORalbVX9SqpF0u6sjAgY9kGy4IZrOEd8wwGZGCQjm2OsYUAzfCAx3KwmTFwzDCeMfYzGM97Fh7DCD0WMzBjLDODx5onsBHGg4WxWrpaepG6u7q7tq69comI98eNzIzKzlZltasqs7p/n3PqZETcG1m3dJWd+ct744YXxzEiIiIiIiIirfxuN0BERERERER6kwKjiIiIiIiItKXAKCIiIiIiIm0pMIqIiIiIiEhbCowiIiIiIiLSlgKjiIiIiIiItKXAKCIiIiIiIm0pMIqIiIiIiEhbCowiIiIiIiLSlgKjiIiIiIiItNWrgTEDHE4eRUREREREpAt6NZBdB5yYmVkiiuJut0VSRkb6mJtb6XYzJEV90nvUJ71J/dJ71Ce9R33Sm9QvvWdiYsDrdht2SkeB0RhzD/AeIAt8yFr7kZby24AHgUHgMeB+a23NGPN24NeB80nVT1tr371VjZedl8kE3W6CtFCf9B71SW9Sv/Qe9UnvUZ/0JvWLdNOGU1KNMQeB9wGvB24D7jPG3NpS7SHgAWvtzYAHvCs5fjvw09ba25IfhUUREREREZFdopNrGO8CPmetnbXWLgOfBN5SLzTGHAKK1trHk0OfAL4/2X418HZjzD8aYx4yxoxsXdNFRERERERkO3UyJfUAMJnanwRes0H5dantfw98Afg14LeAeztt3NhYqdOqsoMmJga63QRpoT7pPeqT3qR+6T3qk96jPulN6hfplk4Cow+kV57xgKiTcmvt99YPGmPeDzy/mcZp0ZveMzExwNTUYrebISnqk96jPulN6pfeoz7pPeqT3qR+6T3XUoDvZErqaWB/an8fcHajcmPMkDHmp1LHPaB2pQ0VERERERGRndVJYPws8AZjzIQxpg+4G/iLeqG19hSwZoy5Izn0VuAzwBLwc8aY1ybHHwD+dMtaLiIiIiIiIttqw8BorT0DvBt4FHgCeNha+0VjzCPGmNuTavcCHzTGPA2UgA9ba0PgB4CPGmOeAl4F/Nx2/BEiIiIiIiKy9Tq6D6O19mHg4ZZj35na/gfWL4RTP/5XwDd9jW0UERERERGRLuhkSqqIiIiIiIhcgxQYRUREREREpC0FRhEREREREWlLgVFERERERETaUmAUERERERGRthQYRUREREREpC0FRhEREREREWlLgVFERERERETaUmAUERERERGRthQYRUREREREpC0FRhEREREREWlLgVFERERERETaUmAUERERERGRthQYRUREREREpC0FRhEREREREWlLgVFERERERETaUmAUERERERGRthQYRUREREREpC0FRhEREREREWlLgVFERERERETaUmAUERERERGRtjKdVDLG3AO8B8gCH7LWfqSl/DbgQWAQeAy431pbS5W/EnjcWpvfqoaLiIiIiIjI9tpwhNEYcxB4H/B64DbgPmPMrS3VHgIesNbeDHjAu1Ln9wG/CeS2qtEiIiIiIiKy/TqZknoX8Dlr7ay1dhn4JPCWeqEx5hBQtNY+nhz6BPD9qfM/AHxoa5orIiIiIiIiO6WTKakHgMnU/iTwmg3KrwMwxnw30Get/aQxZtONGxsrbfoc2X4TEwPdboK0UJ/0HvVJb1K/9B71Se9Rn/Qm9Yt0SyeB0Qfi1L4HRBuVG2P24a57vOtKGzczs0QUxRtXlB0zMTHA1NRit5shKeqT3qM+6U3ql96jPuk96pPepH7pPddSgO9kSuppYH9qfx9wtoPyNwFjwGPGmCcAjDFPGGOunf+6IiIiIiIiu1gnI4yfBd5rjJkAloG7gfvqhdbaU8aYNWPMHdbazwNvBT5jrX0Qt3IqAMaY2Fp729Y2X0RERERERLbLhiOM1tozwLuBR4EngIettV80xjxijLk9qXYv8EFjzNNACfjwdjVYREREREREdkZH92G01j4MPNxy7DtT2//A+oVw2j2HdyUNFBERERERke7o5BpGERERERERuQYpMIqIiIiIiEhbCowiIiIiIiLSlgKjiIiIiIiItKXAKCIiIiIiIm0pMIqIiIiIiEhbCowiIiIiIiLSlgKjiIiIiIiItKXAKCIiIiIiIm0pMIqIiIiIiEhbCowiIiIiIiLSlgKjiIiIiIiItKXAKCIiIiIiIm0pMIqIiIiIiEhbCowiIiIiIiLSlgKjiIiIiIiItKXAKCIiIiIiIm0pMIqIiIiI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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[36]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">facet</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">FacetGrid</span><span class="p">(</span><span class="n">train</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s2">&quot;Survived&quot;</span><span class="p">,</span><span class="n">aspect</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">,</span><span class="s1">&#39;Age&#39;</span><span class="p">,</span><span class="n">shade</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">xlim</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()))</span>
<span class="n">facet</span><span class="o">.</span><span class="n">add_legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlim</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">30</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[36]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(20, 30)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[37]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">facet</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">FacetGrid</span><span class="p">(</span><span class="n">train</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s2">&quot;Survived&quot;</span><span class="p">,</span><span class="n">aspect</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">,</span><span class="s1">&#39;Age&#39;</span><span class="p">,</span><span class="n">shade</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">xlim</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()))</span>
<span class="n">facet</span><span class="o">.</span><span class="n">add_legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlim</span><span class="p">(</span><span class="mi">30</span><span class="p">,</span> <span class="mi">40</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[37]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(30, 40)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">facet</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">FacetGrid</span><span class="p">(</span><span class="n">train</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s2">&quot;Survived&quot;</span><span class="p">,</span><span class="n">aspect</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">,</span><span class="s1">&#39;Age&#39;</span><span class="p">,</span><span class="n">shade</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">xlim</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()))</span>
<span class="n">facet</span><span class="o">.</span><span class="n">add_legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlim</span><span class="p">(</span><span class="mi">40</span><span class="p">,</span> <span class="mi">60</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[38]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(40, 60)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[39]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">facet</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">FacetGrid</span><span class="p">(</span><span class="n">train</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s2">&quot;Survived&quot;</span><span class="p">,</span><span class="n">aspect</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">,</span><span class="s1">&#39;Age&#39;</span><span class="p">,</span><span class="n">shade</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">xlim</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()))</span>
<span class="n">facet</span><span class="o">.</span><span class="n">add_legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlim</span><span class="p">(</span><span class="mi">40</span><span class="p">,</span> <span class="mi">60</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[39]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(40, 60)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA4wAAADQCAYAAABMbu+zAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvnQurowAAIABJREFUeJzt3X2YZVdB5/vvfjmnqrqrX0IoSAID6J1hjcwMRok4CozOQ/ReUBEmIHfI8CIDMWrmKsNVuQaviIOjjrxcHESvkUEn5goyo1cl4AjJY0AIjCOBcQJL9EIkIUDIa3fXyzn75f6x93mp06e7TlWquk53fz/PU8/ee+21du2q1buqf7XW3jup6xpJkiRJkial+30CkiRJkqT5ZGCUJEmSJE1lYJQkSZIkTWVglCRJkiRNZWCUJEmSJE1lYJQkSZIkTWVglCRJkiRNZWCUJEmSJE1lYJQkSZIkTWVglCRJkiRNNa+BMQee0C4lSZIkSftgXgPZY4HP3Xvvcaqq3u9z0ZgLLjjA/fev7vdpaIx9Mn/sk/lkv8wf+2T+2CfzyX6ZPysrh5L9PoczZabAGEJ4EfBaoAO8Jcb4ton9lwLXAYeBW4CrY4xFCOGlwM8DX26rvjfGeO1unbzOvDzP9vsUNME+mT/2yXyyX+aPfTJ/7JP5ZL9oP205JTWE8BjgDcDTgUuBq0IIT5qodj1wTYzxiUACvLItvwz41zHGS9sPw6IkSZIknSVmuYfxcuCmGON9McYTwHuA5w92hhAeDyzFGG9ti94JvKBd/ybgpSGE/x5CuD6EcMHunbokSZIkaS/NMiX1EuDuse27gadusf+xY+u/BHwE+Dng3wNXznpyF164PGtVnUErK4f2+xQ0wT6ZP/bJfLJf5o99Mn/sk/lkv2i/zBIYU2D8yTMJUM2yP8b4vEFhCOEXgb/Zzsn50Jv5s7JyiHvuObbfp6Ex9sn8sU/mk/0yf+yT+WOfzCf7Zf6cTwF+limpdwIXj21fBHxxq/0hhCMhhFeNlSdAsdMTlSRJkiSdWbMExg8AzwwhrIQQDgBXAO8f7Iwx3gGshxCe1ha9GHgfcBz48RDCN7fl1wC/t2tnLkmSJEnaU1sGxhjjXcC1wM3AbcANMcaPhxBuDCFc1la7EnhzCOEzwDLw1hhjCXwf8PYQwqeBpwA/vhdfhCRJkiRp9830HsYY4w3ADRNlzx5b/ySbH4QzKP8Q8I0P8xwlSZIkSftglimpkiRJkqTzkIFRkiRJkjSVgVGSJEmSNJWBUZIkSZI0lYFRkiRJkjSVgVGSJEmSNJWBUZIkSZI0lYFRkiRJkjSVgVGSJEmSNJWBUZIkSZI0lYFRkiRJkjSVgVGSJEmSNJWBUZIkSZI0lYFRkiRJkjSVgVGSJEmSNJWBUZIkSZI0lYFRkiRJkjSVgVGSJEmSNJWBUZIkSZI0lYFRkiRJkjSVgVGSJEmSNFU+S6UQwouA1wId4C0xxrdN7L8UuA44DNwCXB1jLMb2fwNwa4xxYbdOXJIkSZK0t7YcYQwhPAZ4A/B04FLgqhDCkyaqXQ9cE2N8IpAArxxrfwD4ZaC7WyctSZIkSdp7s0xJvRy4KcZ4X4zxBPAe4PmDnSGExwNLMcZb26J3Ai8Ya/9G4C27c7qSJEmSpDNllimplwB3j23fDTx1i/2PBQghPAc4EGN8Twhh2yd34YXL226jvbeycmi/T0ET7JP5Y5/MJ/tl/tgn88c+mU/2i/bLLIExBeqx7QSottofQriI5r7Hy3d6cvfee5yqqreuqDNmZeUQ99xzbL9PQ2Psk/ljn8wn+2X+2Cfzxz6ZT/bL/DmfAvwsU1LvBC4e274I+OIM+78buBC4JYRwG0AI4bYQwvnz3ZUkSZKks9gsI4wfAF4XQlgBTgBXAFcNdsYY7wghrIcQnhZj/DPgxcD7YozX0Tw5FYAQQh1jvHR3T1+SJEmStFe2HGGMMd4FXAvcDNwG3BBj/HgI4cYQwmVttSuBN4cQPgMsA2/dqxOWJEmSJJ0ZM72HMcZ4A3DDRNmzx9Y/yeYH4Uw7RrKTE5QkSZIk7Y9Z7mGUJEmSJJ2HDIySJEmSpKkMjJIkSZKkqQyMkiRJkqSpDIySJEmSpKkMjJIkSZKkqQyMkiRJkqSpDIySJEmSpKkMjJIkSZKkqQyMkiRJkqSpDIySJEmSpKkMjJIkSZKkqQyMkiRJkqSpDIySJEmSpKkMjJIkSZKkqQyMkiRJkqSpDIySJEmSpKkMjJIkSZKkqQyMkiRJkqSpDIySJEmSpKkMjJIkSZKkqfJZKoUQXgS8FugAb4kxvm1i/6XAdcBh4Bbg6hhjEUJ4BvAWoAt8DnhpjPH+XTx/SZIkSdIe2XKEMYTwGOANwNOBS4GrQghPmqh2PXBNjPGJQAK8si3/D8CLY4z/CLgd+LHdOnFJkiRJ0t6aZUrq5cBNMcb7YowngPcAzx/sDCE8HliKMd7aFr0TeEG7/nUxxttDCB3gMYCji5IkSZJ0lphlSuolwN1j23cDT91i/2MBYoz9EMI/Aj4A9IGf3M7JXXjh8naq6wxZWTm036egCfbJ/LFP5pP9Mn/sk/ljn8wn+0X7ZZbAmAL12HYCVLPujzH+d+DRIYQfAN4FfOusJ3fvvcepqnrrijpjVlYOcc89x/b7NDTGPpk/9sl8sl/mj30yf+yT+WS/zJ/zKcDPMiX1TuDise2LgC9utT+EsBhCeO5Y+fXAk3d6opIkSZKkM2uWwPgB4JkhhJUQwgHgCuD9g50xxjuA9RDC09qiFwPvo5mC+rYQwlPa8u8DPrxrZy5JkiRJ2lNbBsYY413AtcDNwG3ADTHGj4cQbgwhXNZWuxJ4cwjhM8Ay8NYYYwm8EPi/Qwi30Two5xV78UVIkiRJknbfTO9hjDHeANwwUfbssfVPsvlBOIPyDwNPmSyXJEmSJM2/WaakSpIkSZLOQwZGSZIkSdJUM01JlSRJkiRtXwjhZcCPABnwIPCvYoy37fBYVwP3xxjftcP2y8BfxhifMGsbA6MkSZIk7YEQwt8BXg08Nca4FkL4FuB3gL+/k+PFGH91N89vFgZGSZIkSdoby0CnXa7FGD8aQvjREMI7gffEGP8ohPDtwDUxxueHEO4A/hb4AvAM4O/FGNdDCC8CvhE4DnwVeBLwZzHG3w4hLAD/AwjAc2jecNEBfj/G+NMhhIM0DzD9GuDPt/sFeA+jJEmSJO2BGOOngVuAO0MIHwwhvBr4yGmaPA74gRjji4APApe35VcAvztW793A89r17wT+BLiQZurr04BvAJ4cQvinwL8C/irG+GTgT7f7NRgYJUmSJGmPxBivAi4F3g+8ALgV6J6i+mqM8fZ2/d3Ac0MIB2hGFD8+Vu8W4OtDCIuMwuQ3A/8A+BjwF8A/bNs9HfjPbbt3AfV2zt/AKEmSJEl7IITwrBDC98QYPx1j/HfAtwBrwMVA0lbrjDVZG1v/E5qw913Ae2OMw6AXY6yAPwaeBfxjmpHDDPjDGOOlMcZLaQLkOyZOqcLAKEmSJElzYR14Qwjh0e32CnAI+Bvg69qy75rWMMbYp5m++lo2T0cdeDfwOuDmGGMJ/FfgO0IIjw4hdID3At9KMxr5wrbNP2ObGdDAKEmSJEl7IMZ4M/BrwIdCCLfTjAq+CvgF4F+EED4B9E5ziHcBR9k8HXXgw8AjacNkjPEu4DXAB4BPATfFGD8I/DJwSQjhL4F/ChTb+RqSut7WiOSZ8gTgc/fee5yqmsvzO2+trBzinnuO7fdpaIx9Mn/sk/lkv8wf+2T+2CfzyX6ZPysrh5Kta50bHGGUJEmSJE1lYJQkSZIkTWVglCRJkiRNZWCUJEmSJE1lYJQkSZIkTWVglCRJkiRNle/3CUiSJEmS9kYI4UXAa4EO8JYY49u2094RRkmSJEk6B4UQHgO8AXg6cClwVQjhSds5hoFRkiRJks5NlwM3xRjvizGeAN4DPH87B3BKqiRJkiTtge959f/7EuDle3T4d/zhG7/3t7aocwlw99j23cBTt/NJZgqMW817DSFcClwHHAZuAa6OMRYhhKcBbwa6wL3Ay2OMd2znBCVJkiRJO5IC9dh2AlTbOcCWgXFs3utTgA3gIyGEm2OMt49Vux54RYzx1hDCbwCvBN4O/DbwnBjjp0IILwfeCnzvdk5QkiRJks5G7QjgVqOAe+lO4Blj2xcBX9zOAWa5h/G0815DCI8HlmKMt7ZF7wReEEJYAF4bY/xUW/4p4HHbOTlJkiRJ0o59AHhmCGElhHAAuAJ4/3YOMMuU1K3mvU7b/9gY4wbNyCMhhBR4HfD72zk5SZIkSdLOxBjvCiFcC9xMc5vgdTHGj2/nGLMExq3mvZ52fwihC/xm+7l+bjsnd+GFy9uprjNkZeXQfp+CJtgn88c+mU/2y/yxT+aPfTKf7BftVIzxBuCGnbafJTBuNe/1TuDiaftDCMvAH9A88OZ7Y4z97Zzcvfcep6rqrSvqjFlZOcQ99xzb79PQGPtk/tgn88l+mT/2yfyxT+aT/TJ/zqcAP8s9jKed99o+9XS9fSIqwIuB97Xr1wN/DbywnaIqSZIkSTpLbBkYY4x3AYN5r7cBN8QYPx5CuDGEcFlb7UrgzSGEzwDLwFtDCN9A80TUpwF/EUK4LYRw4558FZIkSZKkXTfTexinzXuNMT57bP2TnPwCyE/Q3M8oSZIkSToLzTIlVZIkSZJ0HjIwSpIkSZKmMjBKkiRJkqaa6R5GSZIkSdLZKYRwGPgI8N0xxs9vp60jjJIkSZJ0jgohfDPwYeCJO2nvCKMkSZIk7YH/7w1XvAR4+R4d/h1fe+1/+q0Z6r0S+GHgP+7kkxgYJUmSJOkcFWN8BUAIYUftDYySJEmStAfaEcBZRgHn1lwHxrWb3k6dLZIeeTTp4YtIjj6a9NCjSLK5Pm1JkiRJOifMd/LaWKP40qeoN1ZHZUlCemiF9MhFpEceTXLk0e36RSTLjyBJfI6PJEmSJO2GuQ6M3W98Dlm/R91boz5xP9WJ+6lX72/Wj32F4u7PQNEbNchy0sOPJj160WhUsg2UydJhkiTZvy9GkiRJks4ycx0YB5LuEkl3ifSCSzaV13UNG8ebIHnifurVB6iP30f51Tso7rgNqnJUubNEdnRiVPLQCsmhFcOkJEmSpHNajPEJO2l3VgTGU0mSBBYPkS0eggsft2lfXVXUaw9Rn7hvOCpZn7if4oufof7rjwH1qHLWIT30SNJDjyQZLJdXhtvJ4iEDpSRJkqTzzlkdGE8nSVOSg0fh4NGT9tVl0YTI1Qep1x+iXn2Ieu1BqmNfpf7yX1P31jY3GAbKZkQyPXRhEyyXDZSSJEmSzl3nbGA8nSTLSQ6twKGVqfvr/kYzOrn2YLt8iHr1QapjX6H68mdhMlDmC1NGKEfbycKygVKSJEnSWWeuA+NnvrQBRZ/FTsJSJ2Ghk7LYSehkexu+ks4CSWcFDp8uUD44GqEcBMoHv0x1d4T++uYGnYXRCOXyI5sRyuVHki5fSHLgKMmBIyRptqdfkyRJkiRt11wHxt/8yIN85f61k8rzFBY6CUttgGw+0jZYpu2+pnwhH9XZXL9pk6dse/SvCZSPgsOPmrq/7q8PQ2Qz5fXBZsrrA1+i+uKnob8xecTmwTsHj5IevIDkwAWkB4/CgaOkBy4gOXgBycGjjlRKkiRJOqPmOjC+4NIl7j8GvaKmV0CvrOmVNRtFU7bRlm0UFfdvVGyUNRtF89ErZvscWQqLeRMeFzoJC/koaC7kCQudhG6esJg3y0HZwmB9rN6obIH08BaBcvVB6vVj1BsnqNePw8Zx6vXjVA98ifpLn6XeOHFywzQnOXCUdCxYJgePNqOUBy9ow+VRks7iw/iuS5IkSVJjrgPjow9nXNDd2SnWdU2vpA2PTbjcKOtTh88S+kVTdny94v6yoFe2YbWs6Rebnqu6pU5GGzTTiTDZTK1dyBdZyJfotkG0myV0jyR0L6RZTyuW6lUWyxN0y1W65Qny4gRZ7wT1xnHKez5HtfYpKCZHK4HOYhMoDzYjlc201wvasNmOWC4dIcnmuvslSZIk7bNzNjEkScJCDgv57kzhrOuaohoESOiXzbIJkzX9tqxfDsLoqE6/DaervYoHV0dhtde2q06bRBfajws2lXayJlgu5wWPyNe4IF/jaLrKkXSNw6yyfGKVA8fv40D9BRbLE6RUJx25zJeousvUC8uwcAgWD5EsLpMuHSY7cJj8YPORLR1ungSbd3fleylJkiTp7HDOBsbdliQJnQw6WcLBXT52WW0OnP2x7WJsuyhr+tWoXlHV9MucfrnIveVRvlTW9PtjxxkuKxbqDY60gfJIusqRZJXldJ3lZJ3ldI3l5H4OphssJ+tkSZNgi/ZjYKPu8AUWWU0WWU8OsJEu0csO0ssP0M8OUHYOUnaXqbvLlN1lsu4inU5GN8/o5CmdPKWbp3TyrF22ZZ1mO2/3d/OMNPVeTUmSJGm/GRjnQJYmzb2Unb0LSVU1CptF1YTPooJ+CQ9UNV9tA2hR1lBukPXXyMo1snKdTrlBXq3RrdZZYINuucZyfYKV8qsslevkvXLq5yzqlOP1IserBU60y3vrRY5XixyvF1mtu6xVXdbrDmt1d/hRkJGlyVjIzOh20pO3szZ8btrXlI1vd/NsGEYH7afVz7PEhwpJkiRJY2YKjCGEFwGvBTrAW2KMb5vYfylwHXAYuAW4OsZYjO3/WaCMMb5ul85b25SmCQvprFN0u8ChqXuWlxc4fry5b3IdWK9rqPqkxTppf420WCMtN0iLdZL+Gt1ijUf21lgp1kmLB0j7q2RV77SfvSSjny7QSxbpJV3amMp6vcBar8PaRpfVqsNa1eFE1eWessOJMudYP+d42aFHDmw/+CUwFizbUdDOKYJmJ2sD61jwHCsbjaBmE9vtcdrA2+2kZGm67XOVJEmSzoQtA2MI4THAG4CnABvAR0IIN8cYbx+rdj3wihjjrSGE3wBeCbw9hHAEeBPwz4Ff3PWz1/5LEsi6VFmXauHwbG2qkrRYIyk3SIpeEzDLHknVa5ZlU7ZY9lgqNzha9EiKY239DZKq/VtE2n5M/Cuuk5Q6X6TMFinzJYpskSJdpEgX6KUL9JLmo08TLjfqnH6ds17n9OqU9Tplo0xZq3I2qpSirNnoV5xYKyjKqhmJLSqKsqJfVhRFtcV9qKeXJoxGSrNR8Ox2Tg6vg1HVTp4MR1ofcfQAGxt9FtrtwRTfTcvhugFVkiRJs5tlhPFy4KYY430AIYT3AM8HXt9uPx5YijHe2tZ/J/AzwNuB7wU+C7xxd09bZ7U0o+ouA8s7a18VTagsNkjKHslE4EwHZUWPrNwgL9dINh4cBc7y9COc42oSyDrUWZd6caFZ5u0y61JnzXqVdijSLmXSoZ90KOjQT3J6dRNK+zTr/TagbtQ5vSqjqGrKqqIoaoqqaqYKl6Pt1fWCouo15UVFUVX0i0GdaltP7h3I0mQsWGYsdEbTfMfD5UKnHR3tDNabOk0wzVjoNuWDj+5wmZJnhlJJkqRzwSyB8RLg7rHtu4GnbrH/sQAxxt8CCCG8bicnd/Bgl27+MIZutCeWlxf2+QwWYItHD9XA9DsrgaqCcoOk7EP7MVhPqqJZr5r14b6qWQ7rFauw8cCwPWUfih7JNiNcnaSQ5ZB22mUOWRcWcuo0h6wz3N9sN2V12uyvk5yCjJKUgoyCjH6dUtQZ/TqjX6X0SelVKf0qZaNq1jfKpHntTPs6mfWyoNeveWBtVNYvSnr9il5RUm/zMsyyhMVOxkI3Z7GbsbjQLrs5C91sYn28bKzNWPnSQoelheY4Z0sYXVmZPq1b+8t+mT/2yfyxT+aT/aL9MktgTNn8CsIENr2jYav9O3biRI/e+pT3DGrfjN/DeHZLGb6yZDC1tfMwD1nXUJdt6OwNw2dSFSRtAE3qgrTqk5RFU7cuSaqybddsM1iWJUl/dViPqjn2YP9gvVvvyuW2+UvJE+imkGRNqE1S6na9TlIqUmpSqna9qhPKJGuWpJR1MvwoSCl7CcVGQlEnFNXgA4oK1itYJaFqP2oS6nq0PllOmpJlzYOMsiwjyzPyPCfPMvJOs97Jm/VOnjfbnYxuJyfPM7rdDt1OTqebN8tOTppmzfTq9mslTUhIIU03l7frSTKlPG3/ISUJj3rUYe6559iu94senpWVQ/bLnLFP5o99Mp/sl/lzPgX4WQLjncAzxrYvAr44sf/i0+yXzg9JAkk78pcvnrFPu3yww/GHVptQOQiepwihSV2194BWUFckdU1SV0CzTj0qpy6bEdNhWQVt/YRmO6vrZsSW8TrFsN7mttUwVA/3U7dl7b728838yKIa6LcfO1BympHoh+H4MExuDpXJpuB5mvCZNGH1tPtogu3UMDsIrxOBN5k4xvTzSk/+fMNjjwXjwedm4pgkY+d+isCdZu1oekaSdiAbbOckg5H0NGuOIUmS9tUsgfEDwOtCCCvACeAK4KrBzhjjHSGE9RDC02KMfwa8GHjfnpytpJMlaTNNtR0iPScmcQ/D40SIHAuWybQ6Y2VVVbXvMm0fUDS8T7SiLJtXyJTVYL2irGrKsqKqmnplVVNXzb6qvdc0bcY5Saib9QQG461NOaRJRUbdvLc1hU5ak6fNep7W7UfzwzdPKrIEsqQmSyBParKkJk0goyZrP09a18MgPgjY9fj3Y1A2CN/DID4RyOuKejKk15u/h3OlnbKdDKZrp+16NrY+ETSTNBub5p015WkGWYf7Dx2gt162U707JFkH8m6zPli2ZZuXbX0DrCTpPLRlYIwx3hVCuBa4meZ9C9fFGD8eQrgR+D9jjH8OXAn8egjhMPAXwFv38qQlneOSBEg2vR1lMgjPEoxzdu9ls3XdvLu0V9b0isGypldCr6jpl01Zv6zppTn3rBXNdlt3o6jp92CjqDe1nUUCdPOExc7gI22WebO+0BntW8gTFvPNZYt5OtrfSelmnPKdo/WUEV9qNoVOqNt69aayk+oyHmQHwbRqRqXrCqqSul3SjopTjbbrqhzW21Q2XrfsUffXqKsK6pK6HN9fUpfFsG3v4QbiNIe8DZVZlySfFi7b5VgIHW8zLO8sNMt8gaSzQJIvNG3zBegsNIHY98JKkuZAUm/3aRZnxhOAz33ilo/QW1/f73PRmHPnHsZzh30yf2btk6oeBc1e0QTPjbH1flm3DycaD6njoXOwrw2kMwbQNGneybopfHamBM1OwkKejtXdHFYX2vVOdnYEmyNHFnngvuNtgCyaMFn222DZh6qAsoSyoK6KZntQNqg/LBvbHtRvtwfHbZZtne1K0mGATDoLTbAcBM1hwBwPnc1yU72x7c3HWGxGYueA92XNH/tkPtkv82dl5dDZ8ctvF+zWH98lSduUJgkLeRPe2IWHD1dVGzAnAmW/DZMb46Oig3pt3RPrFfcV5XA0dKOoKWcckMtShqOdk8FyPGwujAfSifoLY6OgWbo3v4OTJB1NaWVh9ntlH6a6rofBchQu+9RFry3rN4F1EFqLwXbRjKAOn8ZcUK89RH28oC577TGaJzRvezpx1mlCZGeRZPDRXdq03YTTRcgXSbqLE/sm1jP/OyFJ5yp/wkvSOSJNExZTWOzsThQqq5qNsem34+v9cmxEdMoo6YOrBfeUbZs2gFYzTmjpZGwa7VzaNO02bcNm8zGcqjsx7XY0CpqQ7vPUziRJhvdNAnsSVOuqbF/vMwqfw6BZ9IchdVSnB0WvDa1N6KyO39dO8e1RFxvbC6JpflIApbtI0lk6uXxsufrQBRSrdbtvVK+5Z/S8+eO9JM01A6MkaaosTTjQhQO7EHGG94AWNRtt2BwPmb1ydD/oaP9gu+TExnhwbdrNekNFN2uC42K3uX9zMR9NtV1oR0HH17v5YGQ0bQJpu2+4nid08v0PouOaJ89mTeDapWM2I6PlWLBsl+1H3QbN0WjpIIT2qcsNOPEAdXkPdTEWQKvN86a/dOovaCxkLkwZ/VzcFDJPO/rZXWzuOZ2j/pKks4mBUZK055IkaZ4cmyUc3IXj1fX4NNvT3/85GA2tkpS1jWba7UNrxbDOILDOeg/owCBoDkY5F/LRtNvJELp5e0pYHTvWvASbZmS0ffrswoFdOWY9HkCLHstLKcceeGgYNCnHAugwpPah2KBeO0Z9/N5238ZoSu9sX8xwam2SjwXQ7iJJPgiZbXk+NiLaHU3J3TQ6mi/MTT9J0l4zMEqSzjpJktDNm6fHznr/51YPIxo8hKg/9pChQagc3Afaq8bKJp6Q2ysrjq1X3Ht850F08ETcyUC52ElPCqeD9UH9btasd0+1niWke3R/6MxfX5pBd6kJZkD36AGyzuqOj9cE0NEU22bkszcWQPubysZHRuuN49Sr91P3xwPorC91TYb3eI6PZE6OcA7uBaWzNHFv6NLYtN3F5gFHvrZF0pwyMEqSxO4/hGhg/Gm4g9esDNb75XjgHKwzWi+aIPrgajWcwttvH0xU7OAtIXnKSUFy4XQhM2+egjtt/7DdxL48PfVrW3ZbE0AzEhZ35Xh1XcFgRLPYPNo5eNAQRb+dYtvfNE237q1Srz44GgHtb2wzgHbbULk0CpWDhw3lC5sePDRt1HPz/aELBlBJu8bAKEnSHtrzINre71mUNf1qFEKLsgmV/fHyqq3XjpAW1egpuQ+Um+v2dhhKB6OkmwLmKYLp8oFVKIuZgmknG9XpZHsTTJMkbUcEd+cpuqMA2jvpQUPjDxwajYC293/2+837Rdce3DwFt+jN/snzhdG02slRz/HXtXS6kC8OX8Vy4v6jFKtVu39x+MoWH0Yknb8MjJIknYU2BdE9MrhXtF+NQuhgu2gD5vRQOgqu/cHU3qJidWOivFpr7i/dwSuhEyBv74vtZgl5Nh4soZulzX2z42Gz3TcsS9tlzkSd0XE67bGHy5SZp/bufgCtxx4u1AbMTQ8kakc9y95opHQQSvvr1GsPDcPqMIBOPAn39G+/bkdC88WxwDkePhc3vRd0ON12cF9o3n4v8m5b3h29HzTrkqSOikrzyMAoSZKmGt4rukdvrRzcV1pWpwimE6OiRdUE1GIQWCuGbYtqMKpaU5Ra6df1AAAQPUlEQVQ1D/UqymoUbov2/tOihHIHAXVcmgyCZLtMNwfMUbhs6uRjITRPx0Mo5Onm9cHxssG+tHlicZ5CliXkaU6e5mSdg+QLTVmW7Hy0dXAf6OCdn4eWMh564Fj70KGCuuqd9MqW4TtA22BarT64adR0GF5nfpZxK8s3h8hB2GzD5WB9FDbbsqw7tf60bUdJpe0zMEqSpH2VpQlZCrv3UpDTq+pRiCwGI6LVZFmzLNuAunlJu6+esl6z1qvaYDo45ijkDo6/mxIgS5tgmqWDoLk5dOZp0gTPbBBAk2GbUSjNObDUoSyOjOqPB9Y0IV/g5H3Z5rI8S8iSmpySrO6TV30yCtKqT9K+E3T0btCi/ehTt0uqsfWyoF4/NtyuJ8PrTr5bg2Caddog2SHJxpddkrwDaWe0ng2W7XrWacNr22byWGPbTUh19FRnLwOjJEk6r6R7PHK6lbpupuGOB8lBIB2E1LJuwmk1tl5WTdgt65PLy3pKu/E6dU1RVmz0N9etxgJvU7ZGWdYPexR2upQ06ZKlXfI0IU0hS5rgmg6WbQjNklFZliakyegPC2knIVuAFOimBV0KuklJNynIKYbLDgU55XCZ130ySjJK8rpoQmxdkhYlWb8grVdJ62MkVUFaF+2yJKma4Jpsd8R005eet2Gy0wTWdkk2KOuQpO1rbAZhNctJ2jr3LR+k16ua4wzqZ/lwe/PxNi9JB8dsj2941TYZGCVJks6gJGkCUZbC7tzduHsG04QHobacDJ6nWK+GobXdrk8RettjFnUbnNu6w482FA/aVzX0imps32j/aDulrBOqKh+1Gzvu7qhJqem04bSTlE0YTQo6SUmXkjwp6YyXDT7SpnzYLinpJFUTYpM+ORvkw+020FKNwi0lG5S79i+lIqVKc6okp04yqjSnTvJmmTZl9WC9/SDNIe1QD0Nqs6wHYXUQRsfCbNIG5PH1NG+2003r6fAPAknSvP4nTZo/KKTJ/Lyb9nxmYJQkSdIm46G2LdnP09mxuq6pxwJpOTVwtmUT22W7XrdBdxCiB0G6rqHi5Hbjn2u1huN1U7dm9Hma9ba8Hq1Xdb1p3+CYSZJQVSVpXZLVJUldktZVsz0YKW1DZlpXw7KsLcsZ7C/I6oq8DbyDoJolFR1K8qQgp3fS/kEYHtXfvSHook7pkVLUGQUp5XCZUpBR1CnNV5lR0ayXSTZcVqRUSfuVJjl1klIlOSUZdZpRJVkTiJNmu04mg3GzJGlC7yAgJ2lGMgyvyaZAm6UJP3DF1+/a92DeGRglSZJ0TkqShCRppq+Ole7T2ezcYOR3Nw3DNJOhtQmpvRrW68lwW7chumpeG1OWUJdQFVCVUDVhNqma8qQqSShJqmpsuxqVt6E3qcfXK5K6IK0rupQstuUp/WZZN8fI6pK0DchtjBz17CDPlg/ve1QMQutEkO2TwRXXPbyDn0UMjJIkSdJ5ZnqYHu7donW2+yd0GjVN9jtt/qvb4eC6IqnHAmtdDYMsdTUKs3UJVRNGm+161G5wjLZdXld0qlH7pH6YSfQsY2CUJEmSdHZLEkgyIKOmA2z7xS46BR+TJEmSJEmaysAoSZIkSZrKwChJkiRJmsrAKEmSJEmaysAoSZIkSZpqpqekhhBeBLwW6ABviTG+bWL/pcB1wGHgFuDqGGMRQngccD3wKCACV8YYj+/i+UuSJEmS9siWI4whhMcAbwCeDlwKXBVCeNJEteuBa2KMT6R5ccsr2/JfAX4lxvj3gT8Hfmq3TlySJEmStLdmGWG8HLgpxngfQAjhPcDzgde3248HlmKMt7b13wn8TAjhOuCfAM8dK/9T4Cdm+JwZwIGDS3RyZ83Ok8WlBeoz/LJWnZ59Mn/sk/lkv8wf+2T+2CfzyX6ZS08A7gSKfT6PPTdLYLwEuHts+27gqVvsfyzwSOChGGMxUT6LiwHCU75hxuqSJEmSdMZ8Dvga4PP7fB57bpbAmAL12HYCVDPsnyxnot3p/FfgGTQhs5yxjSRJkiSdKXfu9wmcCbMExjtpwtvARcAXJ/ZfPGX/V4AjIYQsxli2dcbbnc4G8OEZ60qSJEmS9sAsNwh+AHhmCGElhHAAuAJ4/2BnjPEOYD2E8LS26MXA+2KMfeBDwAvb8pcA79u1M5ckSZIk7aktA2OM8S7gWuBm4Dbghhjjx0MIN4YQLmurXQm8OYTwGWAZeGtb/kM0T1W9nWaU8rW7/QVIkiRJkvZGUteTtxlKkiRJkjTblFRJkiRJ0nnIwChJkiRJmsrAKEmSJEmaysAoSZIkSZrKwChJkiRJmirfz08eQvgl4JExxpeFEC4FrgMOA7cAV8cYi4n6R4HfBr4WuAf4vhjjl87waZ/TJvrke4GfARLgc8D3xxjvn6j/bcB/Br7QFn0ixvj9Z/Kcz3UTffLTwMuBQT/8eozxbRP1HwdcDzwKiMCVMcbjZ/KczweDfgHeArxzbNcKcH+M8R9O1Pda2SMhhJtp/r3326IfAP4nmlc5dYC3TF4nbbstf+9o507RL/8L8H3t9ntjjD8+pd2WP+e0M6fok5+fLIsxfmyi3eXAm4Al4F0xRl+Ttkum9Mn/A/zzsSpfA/zHGOM1E+28TvZQCOF7gJ8GDgL/Jcb4I7NcB+fq/8H2LTCGEJ4JvBR4b1t0PfCKGOOtIYTfAF4JvH2i2b8BPhRj/K4QwouB/wt44Zk653PdeJ+EEA7TfP+/KcZ4Vwjh9cDrgB+ZaHYZ8Esxxn97Rk/2PDHlOrkM+F9jjB89TbNfAX4lxvg7IYSfAn4K+Im9PdPzy3i/xBhvAy5tyw8AHweuntLMa2UPhBAS4InA4wdhL4TwGOB3gKcAG8BHQgg3xxhvn2g+y+8d7cAp+uVy4DuBbwBq4P0hhOfFGH9vovksP+e0Tafok5PKprRbAt4BfBvNH7zeG0J4VozxfWfmzM9dp/n+/0K7/x8Av0/z/69JXid7JITwtcCvAt8MfBm4KYTwLODX2Po6OCf/D7YvU1JDCI8A3gD8XLv9eGApxnhrW+WdwAumNP0umhFGaP4C86wQQmdvz/b8MNknNH+V/+EY413t9qeAx01p+k3Ad4YQPhVC+IMQwt/Z+7M9P0zpE2h+Qfxk+/3+9yGExYk2HeCfAO9pi97J9GtJO3SKfhn4P4A/jTF+eMo+r5W9EdrlfwkhfDKEcA1wOXBTjPG+GOMJmuvh+Zsazf57RzszrV/uBl4dY+zFGPvAp5n+e+W0P+e0Y9P6ZFrZpKcCn40xfq4NNdfjtbJbtvr+vx34yRjjV6e09TrZO8+jGUG8s/1Z9UJglS2ug3P5/2D7dQ/jrwHXMhpGv4TmF8nA3cBjp7Qb1ms76yGa6V96+Db1SYzx3sFffdu/Lr6G5q9ckx4AfjnG+GTgRpq/6mt3bOqTEMIy8Angx4BvBI7S/OVq3COBh8b+Unmqa0k7N/nzC4AQwhHgKppp3NN4reyNC4AP0vyCfybN6O7j2Pp3yqy/d7Qz0/rlkkFADyH8PZqpqTeON5rx55x2ZlqfvGCyLITwHRPtvFb2zkl9Mvj+tyPySzHG351s5HWy5/4ukLV/3L0N+CFmuw7O2f+DnfEpqSGEVwBfiDF+MITwsrY4pZmeMpAA1ZTmyZTtafW0Dafok8G+I8DvAZ+MMf7mZNsY49Vj678aQvj5EMKRGOODe33e57JpfdLOgX/2WJ030kwTunas6eS1BF4ju+Z01wrwL4DfjzF+ZVpbr5W90U7HGk7JaqeWvonmFoaBab8rZv29ox04Rb88G/iTdprde4EfizF+dqLdLD/ntAOn6JPHxRhfMlH2bOBPxpp6reyR010nNPeXvukU7bxO9lZOM1L47cBx4A+ANba+Ds7Z/4Ptxz2MLwQubhP7I4Blmm/uxWN1LgK+OKXtXe2+O0MIOXAIuHdvT/e8cFKfhBDeDPwi8MfATcCrJhuFEFKaKXg/H2Msx3b50IiHb1qf/Aeae3jf0dZJGN0kP/AV4EgIIWv75GKmX0vamanXSozxVcBzmT5N1WtlD4UQng4sxBg/2BYlwOfZ+nfKnTPU0Q6dol/6IYSnAf8J+NEY40mj7O0DIy7f4uecduAUffL1IYRnTvbTRFOvlT1ymuukS3Ov3MtO0c7rZG99CfhAjPEegBDC79GMxo///p52HZyz/wc744Exxjic6tD+hf7bY4zfH0L4yxDC02KMfwa8GJh2M/WNwEto/lP2Qpr/PHuBPEzT+gT434GPAe+OMf6bU7SrQgjPAz4LvDuE8BLgY+09Q3oYTtEnPw58un2i2ueBH6YZ/R1v1w8hfIjm+riB5nrxwQS75BQ/v17VPrjgKYz9pXiindfK3jkKvD6E8K00916/lGa09/oQwgpwAriCZrrwUIzxjhDC+gy/d7Qz0/rlGppbG14YY7zpFO3WgF883c857di0PnkP8O8myiYf2vUxIIQQ/i7NE9NfRDOapYdvWp9cDTwZ+KvT/I7wOtlbfwT8ZmjeznAMeBbNtfKa010H5/L/webpPYxXAm8OIXyGZtTxrQAhhNeHEAY/vH4K+MchhP9BM5/4h/flTM8Pz6GZF//8EMJt7cd1cFKfvBT40bZPvh94xf6c7rmv/UvXDwB/SPOo5gR4I0AI4boQwnPaqj8EXBVCuB14Bs2rBbS3VoBejHF9vNBrZe/FGP+IZnrjJ4D/BryjDYDXAjcDtwE3xBg/DhBCuDGEcFnbfOrvHT180/qF5sFDi8Cbxn6vXA2jfjndzzk9PKe4Vn52StlHAdr+uaT9ufYympHh24HPMHqohx6GU/TJR2leH3fnZH2vkzOjfa3MLwIfpvk3fwfNA4hexpTr4Hz4P1hS15NTbSVJkiRJmq8RRkmSJEnSHDEwSpIkSZKmMjBKkiRJkqYyMEqSJEmSpjIwSpIkSZKmOuPvYZQkaS+EEDrA3wK3xRiftd/nI0nSucARRknSueKf0bx38bIQwtft98lIknQucIRRknSu+EHgd4C/AX4EGLwU/jXAvwSOAbcAz40xPiGE0AV+Afg2IKN5efb/FmN8aB/OXZKkueQIoyTprBdCeBLwLcDvAr8JvCSEcGEI4X8GXgZ8E/AU4NBYs9cABfCUGOPXA18Efv5MnrckSfPOEUZJ0rngB4E/ijHeC9wbQvgccBVwEfC7McYHAEIIbwOe2bb5buAo8B0hBIAu8JUzfeKSJM0zA6Mk6awWQjgIvBjYCCF8vi0+DFxDM0U1Gatejq1nwI/EGN/XHmcZWNzr85Uk6WzilFRJ0tnuSuBe4JIY4xNijE8AvhZYBv4bcEUI4Uhb918Cdbv+x8A1IYRuCCEFfh34t2f0zCVJmnMGRknS2e4HgTfFGIejh+0U1LcCr6IJgh8NIfw5cARYbav9LPB5mofd3E4zEvnqM3fakiTNv6Su661rSZJ0FgohXAZ8a4zxre32vwa+Ocb4wv09M0mSzg7ewyhJOpf9FfATIYSraKai/i3Nw3AkSdIMHGGUJEmSJE3lPYySJEmSpKkMjJIkSZKkqQyMkiRJkqSpDIySJEmSpKkMjJIkSZKkqf5/vIubEVsa8SMAAAAASUVORK5CYII=
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[40]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">facet</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">FacetGrid</span><span class="p">(</span><span class="n">train</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s2">&quot;Survived&quot;</span><span class="p">,</span><span class="n">aspect</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">,</span><span class="s1">&#39;Age&#39;</span><span class="p">,</span><span class="n">shade</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">xlim</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()))</span>
<span class="n">facet</span><span class="o">.</span><span class="n">add_legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlim</span><span class="p">(</span><span class="mi">60</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[40]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(60, 80.0)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[41]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
PassengerId    891 non-null int64
Survived       891 non-null int64
Pclass         891 non-null int64
Sex            891 non-null int64
Age            891 non-null float64
SibSp          891 non-null int64
Parch          891 non-null int64
Ticket         891 non-null object
Fare           891 non-null float64
Cabin          204 non-null object
Embarked       889 non-null object
Title          891 non-null int64
dtypes: float64(2), int64(7), object(3)
memory usage: 73.1+ KB
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[42]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">test</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 418 entries, 0 to 417
Data columns (total 11 columns):
PassengerId    418 non-null int64
Pclass         418 non-null int64
Sex            418 non-null int64
Age            418 non-null float64
SibSp          418 non-null int64
Parch          418 non-null int64
Ticket         418 non-null object
Fare           417 non-null float64
Cabin          91 non-null object
Embarked       418 non-null object
Title          418 non-null int64
dtypes: float64(2), int64(6), object(3)
memory usage: 31.1+ KB
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="4.4.2-Binning">4.4.2 Binning<a class="anchor-link" href="#4.4.2-Binning">&#182;</a></h4><p>Binning/Converting Numerical Age to Categorical Variable</p>
<p>feature vector map:<br>
child: 0<br>
young: 1<br>
adult: 2<br>
mid-age: 3<br>
senior: 4</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[43]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">dataset</span> <span class="ow">in</span> <span class="n">train_test_data</span><span class="p">:</span>
    <span class="n">dataset</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span> <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="mi">16</span><span class="p">,</span> <span class="s1">&#39;Age&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="n">dataset</span><span class="o">.</span><span class="n">loc</span><span class="p">[(</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">16</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="mi">26</span><span class="p">),</span> <span class="s1">&#39;Age&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="n">dataset</span><span class="o">.</span><span class="n">loc</span><span class="p">[(</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">26</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="mi">36</span><span class="p">),</span> <span class="s1">&#39;Age&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
    <span class="n">dataset</span><span class="o">.</span><span class="n">loc</span><span class="p">[(</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">36</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="mi">62</span><span class="p">),</span> <span class="s1">&#39;Age&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
    <span class="n">dataset</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span> <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">62</span><span class="p">,</span> <span class="s1">&#39;Age&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">4</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[44]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[44]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[45]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">bar_chart</span><span class="p">(</span><span class="s1">&#39;Age&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="4.5-Embarked">4.5 Embarked<a class="anchor-link" href="#4.5-Embarked">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="4.5.1-filling-missing-values">4.5.1 filling missing values<a class="anchor-link" href="#4.5.1-filling-missing-values">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[46]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Pclass1</span> <span class="o">=</span> <span class="n">train</span><span class="p">[</span><span class="n">train</span><span class="p">[</span><span class="s1">&#39;Pclass&#39;</span><span class="p">]</span><span class="o">==</span><span class="mi">1</span><span class="p">][</span><span class="s1">&#39;Embarked&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
<span class="n">Pclass2</span> <span class="o">=</span> <span class="n">train</span><span class="p">[</span><span class="n">train</span><span class="p">[</span><span class="s1">&#39;Pclass&#39;</span><span class="p">]</span><span class="o">==</span><span class="mi">2</span><span class="p">][</span><span class="s1">&#39;Embarked&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
<span class="n">Pclass3</span> <span class="o">=</span> <span class="n">train</span><span class="p">[</span><span class="n">train</span><span class="p">[</span><span class="s1">&#39;Pclass&#39;</span><span class="p">]</span><span class="o">==</span><span class="mi">3</span><span class="p">][</span><span class="s1">&#39;Embarked&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">([</span><span class="n">Pclass1</span><span class="p">,</span> <span class="n">Pclass2</span><span class="p">,</span> <span class="n">Pclass3</span><span class="p">])</span>
<span class="n">df</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;1st class&#39;</span><span class="p">,</span><span class="s1">&#39;2nd class&#39;</span><span class="p">,</span> <span class="s1">&#39;3rd class&#39;</span><span class="p">]</span>
<span class="n">df</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">&#39;bar&#39;</span><span class="p">,</span><span class="n">stacked</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">5</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[46]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x4c9e370&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>more than 50% of 1st class are from S embark<br>
more than 50% of 2nd class are from S embark<br>
more than 50% of 3rd class are from S embark</p>
<p><strong>fill out missing embark with S embark</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[47]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">dataset</span> <span class="ow">in</span> <span class="n">train_test_data</span><span class="p">:</span>
    <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Embarked&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Embarked&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="s1">&#39;S&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[48]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[48]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[49]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">embarked_mapping</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;S&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s2">&quot;C&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s2">&quot;Q&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">}</span>
<span class="k">for</span> <span class="n">dataset</span> <span class="ow">in</span> <span class="n">train_test_data</span><span class="p">:</span>
    <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Embarked&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Embarked&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">embarked_mapping</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="4.6-Fare">4.6 Fare<a class="anchor-link" href="#4.6-Fare">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[50]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># fill missing Fare with median fare for each Pclass</span>
<span class="n">train</span><span class="p">[</span><span class="s2">&quot;Fare&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">train</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">&quot;Pclass&quot;</span><span class="p">)[</span><span class="s2">&quot;Fare&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="s2">&quot;median&quot;</span><span class="p">),</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">test</span><span class="p">[</span><span class="s2">&quot;Fare&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">&quot;Pclass&quot;</span><span class="p">)[</span><span class="s2">&quot;Fare&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="s2">&quot;median&quot;</span><span class="p">),</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">train</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[50]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>330877</td>
      <td>8.4583</td>
      <td>NaN</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>3.0</td>
      <td>0</td>
      <td>0</td>
      <td>17463</td>
      <td>51.8625</td>
      <td>E46</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0.0</td>
      <td>3</td>
      <td>1</td>
      <td>349909</td>
      <td>21.0750</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>2.0</td>
      <td>0</td>
      <td>2</td>
      <td>347742</td>
      <td>11.1333</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>237736</td>
      <td>30.0708</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[51]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">facet</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">FacetGrid</span><span class="p">(</span><span class="n">train</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s2">&quot;Survived&quot;</span><span class="p">,</span><span class="n">aspect</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">,</span><span class="s1">&#39;Fare&#39;</span><span class="p">,</span><span class="n">shade</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">xlim</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;Fare&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()))</span>
<span class="n">facet</span><span class="o">.</span><span class="n">add_legend</span><span class="p">()</span>

<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>  
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[52]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">facet</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">FacetGrid</span><span class="p">(</span><span class="n">train</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s2">&quot;Survived&quot;</span><span class="p">,</span><span class="n">aspect</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">,</span><span class="s1">&#39;Fare&#39;</span><span class="p">,</span><span class="n">shade</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">xlim</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;Fare&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()))</span>
<span class="n">facet</span><span class="o">.</span><span class="n">add_legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlim</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">20</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[52]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(0, 20)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[53]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">facet</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">FacetGrid</span><span class="p">(</span><span class="n">train</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s2">&quot;Survived&quot;</span><span class="p">,</span><span class="n">aspect</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">,</span><span class="s1">&#39;Fare&#39;</span><span class="p">,</span><span class="n">shade</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">xlim</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;Fare&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()))</span>
<span class="n">facet</span><span class="o">.</span><span class="n">add_legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlim</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">30</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[53]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(0, 30)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[54]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">facet</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">FacetGrid</span><span class="p">(</span><span class="n">train</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s2">&quot;Survived&quot;</span><span class="p">,</span><span class="n">aspect</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">,</span><span class="s1">&#39;Fare&#39;</span><span class="p">,</span><span class="n">shade</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">xlim</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;Fare&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()))</span>
<span class="n">facet</span><span class="o">.</span><span class="n">add_legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlim</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[54]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(0, 512.3292)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[55]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">dataset</span> <span class="ow">in</span> <span class="n">train_test_data</span><span class="p">:</span>
    <span class="n">dataset</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span> <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Fare&#39;</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="mi">17</span><span class="p">,</span> <span class="s1">&#39;Fare&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="n">dataset</span><span class="o">.</span><span class="n">loc</span><span class="p">[(</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Fare&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">17</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Fare&#39;</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="mi">30</span><span class="p">),</span> <span class="s1">&#39;Fare&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="n">dataset</span><span class="o">.</span><span class="n">loc</span><span class="p">[(</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Fare&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">30</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Fare&#39;</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="mi">100</span><span class="p">),</span> <span class="s1">&#39;Fare&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
    <span class="n">dataset</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span> <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Fare&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">100</span><span class="p">,</span> <span class="s1">&#39;Fare&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[56]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[56]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>2.0</td>
      <td>C85</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>2.0</td>
      <td>C123</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="4.7-Cabin">4.7 Cabin<a class="anchor-link" href="#4.7-Cabin">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[57]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">Cabin</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[57]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>G6                 4
C23 C25 C27        4
B96 B98            4
D                  3
C22 C26            3
F33                3
F2                 3
E101               3
C83                2
C68                2
B22                2
C123               2
D26                2
B58 B60            2
B49                2
C65                2
C2                 2
C52                2
D33                2
E44                2
B77                2
B35                2
C126               2
D35                2
D20                2
E25                2
B57 B59 B63 B66    2
C124               2
C92                2
D17                2
                  ..
A34                1
E36                1
C104               1
B101               1
E46                1
C54                1
C110               1
D9                 1
C86                1
B79                1
C50                1
B39                1
C49                1
A24                1
E38                1
A26                1
A5                 1
C30                1
E40                1
C62 C64            1
B82 B84            1
F E69              1
A10                1
C7                 1
C128               1
C90                1
B41                1
C91                1
D46                1
A32                1
Name: Cabin, Length: 147, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[58]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">dataset</span> <span class="ow">in</span> <span class="n">train_test_data</span><span class="p">:</span>
    <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Cabin&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Cabin&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="p">[:</span><span class="mi">1</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[59]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Pclass1</span> <span class="o">=</span> <span class="n">train</span><span class="p">[</span><span class="n">train</span><span class="p">[</span><span class="s1">&#39;Pclass&#39;</span><span class="p">]</span><span class="o">==</span><span class="mi">1</span><span class="p">][</span><span class="s1">&#39;Cabin&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
<span class="n">Pclass2</span> <span class="o">=</span> <span class="n">train</span><span class="p">[</span><span class="n">train</span><span class="p">[</span><span class="s1">&#39;Pclass&#39;</span><span class="p">]</span><span class="o">==</span><span class="mi">2</span><span class="p">][</span><span class="s1">&#39;Cabin&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
<span class="n">Pclass3</span> <span class="o">=</span> <span class="n">train</span><span class="p">[</span><span class="n">train</span><span class="p">[</span><span class="s1">&#39;Pclass&#39;</span><span class="p">]</span><span class="o">==</span><span class="mi">3</span><span class="p">][</span><span class="s1">&#39;Cabin&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">([</span><span class="n">Pclass1</span><span class="p">,</span> <span class="n">Pclass2</span><span class="p">,</span> <span class="n">Pclass3</span><span class="p">])</span>
<span class="n">df</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;1st class&#39;</span><span class="p">,</span><span class="s1">&#39;2nd class&#39;</span><span class="p">,</span> <span class="s1">&#39;3rd class&#39;</span><span class="p">]</span>
<span class="n">df</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">&#39;bar&#39;</span><span class="p">,</span><span class="n">stacked</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">5</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[59]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x12784910&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[60]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">cabin_mapping</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;A&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s2">&quot;B&quot;</span><span class="p">:</span> <span class="mf">0.4</span><span class="p">,</span> <span class="s2">&quot;C&quot;</span><span class="p">:</span> <span class="mf">0.8</span><span class="p">,</span> <span class="s2">&quot;D&quot;</span><span class="p">:</span> <span class="mf">1.2</span><span class="p">,</span> <span class="s2">&quot;E&quot;</span><span class="p">:</span> <span class="mf">1.6</span><span class="p">,</span> <span class="s2">&quot;F&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span> <span class="s2">&quot;G&quot;</span><span class="p">:</span> <span class="mf">2.4</span><span class="p">,</span> <span class="s2">&quot;T&quot;</span><span class="p">:</span> <span class="mf">2.8</span><span class="p">}</span>
<span class="k">for</span> <span class="n">dataset</span> <span class="ow">in</span> <span class="n">train_test_data</span><span class="p">:</span>
    <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Cabin&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Cabin&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">cabin_mapping</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[61]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># fill missing Fare with median fare for each Pclass</span>
<span class="n">train</span><span class="p">[</span><span class="s2">&quot;Cabin&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">train</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">&quot;Pclass&quot;</span><span class="p">)[</span><span class="s2">&quot;Cabin&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="s2">&quot;median&quot;</span><span class="p">),</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">test</span><span class="p">[</span><span class="s2">&quot;Cabin&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">&quot;Pclass&quot;</span><span class="p">)[</span><span class="s2">&quot;Cabin&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="s2">&quot;median&quot;</span><span class="p">),</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="4.8-FamilySize">4.8 FamilySize<a class="anchor-link" href="#4.8-FamilySize">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[62]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="p">[</span><span class="s2">&quot;FamilySize&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">train</span><span class="p">[</span><span class="s2">&quot;SibSp&quot;</span><span class="p">]</span> <span class="o">+</span> <span class="n">train</span><span class="p">[</span><span class="s2">&quot;Parch&quot;</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span>
<span class="n">test</span><span class="p">[</span><span class="s2">&quot;FamilySize&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">test</span><span class="p">[</span><span class="s2">&quot;SibSp&quot;</span><span class="p">]</span> <span class="o">+</span> <span class="n">test</span><span class="p">[</span><span class="s2">&quot;Parch&quot;</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[63]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">facet</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">FacetGrid</span><span class="p">(</span><span class="n">train</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s2">&quot;Survived&quot;</span><span class="p">,</span><span class="n">aspect</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">,</span><span class="s1">&#39;FamilySize&#39;</span><span class="p">,</span><span class="n">shade</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">facet</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">xlim</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;FamilySize&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()))</span>
<span class="n">facet</span><span class="o">.</span><span class="n">add_legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlim</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[63]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(0, 11.0)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[64]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">family_mapping</span> <span class="o">=</span> <span class="p">{</span><span class="mi">1</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">2</span><span class="p">:</span> <span class="mf">0.4</span><span class="p">,</span> <span class="mi">3</span><span class="p">:</span> <span class="mf">0.8</span><span class="p">,</span> <span class="mi">4</span><span class="p">:</span> <span class="mf">1.2</span><span class="p">,</span> <span class="mi">5</span><span class="p">:</span> <span class="mf">1.6</span><span class="p">,</span> <span class="mi">6</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">7</span><span class="p">:</span> <span class="mf">2.4</span><span class="p">,</span> <span class="mi">8</span><span class="p">:</span> <span class="mf">2.8</span><span class="p">,</span> <span class="mi">9</span><span class="p">:</span> <span class="mf">3.2</span><span class="p">,</span> <span class="mi">10</span><span class="p">:</span> <span class="mf">3.6</span><span class="p">,</span> <span class="mi">11</span><span class="p">:</span> <span class="mi">4</span><span class="p">}</span>
<span class="k">for</span> <span class="n">dataset</span> <span class="ow">in</span> <span class="n">train_test_data</span><span class="p">:</span>
    <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;FamilySize&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;FamilySize&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">family_mapping</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[65]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[65]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
      <th>FamilySize</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>2.0</td>
      <td>0.8</td>
      <td>1</td>
      <td>2</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>2.0</td>
      <td>0.8</td>
      <td>0</td>
      <td>2</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[66]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[66]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
      <th>FamilySize</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>2.0</td>
      <td>0.8</td>
      <td>1</td>
      <td>2</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>2.0</td>
      <td>0.8</td>
      <td>0</td>
      <td>2</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[67]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">features_drop</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Ticket&#39;</span><span class="p">,</span> <span class="s1">&#39;SibSp&#39;</span><span class="p">,</span> <span class="s1">&#39;Parch&#39;</span><span class="p">]</span>
<span class="n">train</span> <span class="o">=</span> <span class="n">train</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">features_drop</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">test</span> <span class="o">=</span> <span class="n">test</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">features_drop</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">train</span> <span class="o">=</span> <span class="n">train</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;PassengerId&#39;</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[68]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train_data</span> <span class="o">=</span> <span class="n">train</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s1">&#39;Survived&#39;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">target</span> <span class="o">=</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;Survived&#39;</span><span class="p">]</span>

<span class="n">train_data</span><span class="o">.</span><span class="n">shape</span><span class="p">,</span> <span class="n">target</span><span class="o">.</span><span class="n">shape</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[68]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>((891, 8), (891,))</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[69]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train_data</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[69]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
      <th>FamilySize</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>0.8</td>
      <td>1</td>
      <td>2</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>0.8</td>
      <td>0</td>
      <td>2</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>2</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1</td>
      <td>0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.6</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>0</td>
      <td>3</td>
      <td>1.6</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3</td>
      <td>1</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0</td>
      <td>2</td>
      <td>0.8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2</td>
      <td>1</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>1.8</td>
      <td>1</td>
      <td>2</td>
      <td>0.4</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="5.-Modelling">5. Modelling<a class="anchor-link" href="#5.-Modelling">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[70]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Importing Classifier Modules</span>
<span class="kn">from</span> <span class="nn">sklearn.neighbors</span> <span class="k">import</span> <span class="n">KNeighborsClassifier</span>
<span class="kn">from</span> <span class="nn">sklearn.tree</span> <span class="k">import</span> <span class="n">DecisionTreeClassifier</span>
<span class="kn">from</span> <span class="nn">sklearn.ensemble</span> <span class="k">import</span> <span class="n">RandomForestClassifier</span>
<span class="kn">from</span> <span class="nn">sklearn.naive_bayes</span> <span class="k">import</span> <span class="n">GaussianNB</span>
<span class="kn">from</span> <span class="nn">sklearn.svm</span> <span class="k">import</span> <span class="n">SVC</span>

<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[73]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 891 entries, 0 to 890
Data columns (total 9 columns):
Survived      891 non-null int64
Pclass        891 non-null int64
Sex           891 non-null int64
Age           891 non-null float64
Fare          891 non-null float64
Cabin         891 non-null float64
Embarked      891 non-null int64
Title         891 non-null int64
FamilySize    891 non-null float64
dtypes: float64(4), int64(5)
memory usage: 62.7 KB
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="6.2-Cross-Validation-(K-fold)">6.2 Cross Validation (K-fold)<a class="anchor-link" href="#6.2-Cross-Validation-(K-fold)">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[71]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="k">import</span> <span class="n">KFold</span>
<span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="k">import</span> <span class="n">cross_val_score</span>
<span class="n">k_fold</span> <span class="o">=</span> <span class="n">KFold</span><span class="p">(</span><span class="n">n_splits</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">shuffle</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="6.2.1-kNN">6.2.1 kNN<a class="anchor-link" href="#6.2.1-kNN">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[72]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">clf</span> <span class="o">=</span> <span class="n">KNeighborsClassifier</span><span class="p">(</span><span class="n">n_neighbors</span> <span class="o">=</span> <span class="mi">13</span><span class="p">)</span>
<span class="n">scoring</span> <span class="o">=</span> <span class="s1">&#39;accuracy&#39;</span>
<span class="n">score</span> <span class="o">=</span> <span class="n">cross_val_score</span><span class="p">(</span><span class="n">clf</span><span class="p">,</span> <span class="n">train_data</span><span class="p">,</span> <span class="n">target</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="n">k_fold</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">scoring</span><span class="o">=</span><span class="n">scoring</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">score</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[0.82222222 0.76404494 0.80898876 0.83146067 0.87640449 0.82022472
 0.85393258 0.79775281 0.84269663 0.84269663]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[73]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># kNN Score</span>
<span class="nb">round</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">score</span><span class="p">)</span><span class="o">*</span><span class="mi">100</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[73]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>82.6</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="6.2.2-Decision-Tree">6.2.2 Decision Tree<a class="anchor-link" href="#6.2.2-Decision-Tree">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[74]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">clf</span> <span class="o">=</span> <span class="n">DecisionTreeClassifier</span><span class="p">()</span>
<span class="n">scoring</span> <span class="o">=</span> <span class="s1">&#39;accuracy&#39;</span>
<span class="n">score</span> <span class="o">=</span> <span class="n">cross_val_score</span><span class="p">(</span><span class="n">clf</span><span class="p">,</span> <span class="n">train_data</span><span class="p">,</span> <span class="n">target</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="n">k_fold</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">scoring</span><span class="o">=</span><span class="n">scoring</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">score</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[0.76666667 0.82022472 0.75280899 0.7752809  0.87640449 0.75280899
 0.83146067 0.82022472 0.74157303 0.79775281]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[75]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># decision tree Score</span>
<span class="nb">round</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">score</span><span class="p">)</span><span class="o">*</span><span class="mi">100</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[75]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>79.35</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="6.2.3-Ramdom-Forest">6.2.3 Ramdom Forest<a class="anchor-link" href="#6.2.3-Ramdom-Forest">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[76]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">clf</span> <span class="o">=</span> <span class="n">RandomForestClassifier</span><span class="p">(</span><span class="n">n_estimators</span><span class="o">=</span><span class="mi">13</span><span class="p">)</span>
<span class="n">scoring</span> <span class="o">=</span> <span class="s1">&#39;accuracy&#39;</span>
<span class="n">score</span> <span class="o">=</span> <span class="n">cross_val_score</span><span class="p">(</span><span class="n">clf</span><span class="p">,</span> <span class="n">train_data</span><span class="p">,</span> <span class="n">target</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="n">k_fold</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">scoring</span><span class="o">=</span><span class="n">scoring</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">score</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[0.78888889 0.80898876 0.83146067 0.75280899 0.85393258 0.78651685
 0.82022472 0.79775281 0.73033708 0.79775281]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[77]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Random Forest Score</span>
<span class="nb">round</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">score</span><span class="p">)</span><span class="o">*</span><span class="mi">100</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[77]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>79.69</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="6.2.4-Naive-Bayes">6.2.4 Naive Bayes<a class="anchor-link" href="#6.2.4-Naive-Bayes">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[78]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">clf</span> <span class="o">=</span> <span class="n">GaussianNB</span><span class="p">()</span>
<span class="n">scoring</span> <span class="o">=</span> <span class="s1">&#39;accuracy&#39;</span>
<span class="n">score</span> <span class="o">=</span> <span class="n">cross_val_score</span><span class="p">(</span><span class="n">clf</span><span class="p">,</span> <span class="n">train_data</span><span class="p">,</span> <span class="n">target</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="n">k_fold</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">scoring</span><span class="o">=</span><span class="n">scoring</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">score</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[0.85555556 0.73033708 0.75280899 0.75280899 0.70786517 0.80898876
 0.76404494 0.80898876 0.86516854 0.83146067]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[79]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Naive Bayes Score</span>
<span class="nb">round</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">score</span><span class="p">)</span><span class="o">*</span><span class="mi">100</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[79]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>78.78</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="6.2.5-SVM">6.2.5 SVM<a class="anchor-link" href="#6.2.5-SVM">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">clf</span> <span class="o">=</span> <span class="n">SVC</span><span class="p">()</span>
<span class="n">scoring</span> <span class="o">=</span> <span class="s1">&#39;accuracy&#39;</span>
<span class="n">score</span> <span class="o">=</span> <span class="n">cross_val_score</span><span class="p">(</span><span class="n">clf</span><span class="p">,</span> <span class="n">train_data</span><span class="p">,</span> <span class="n">target</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="n">k_fold</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">scoring</span><span class="o">=</span><span class="n">scoring</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">score</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[81]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">round</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">score</span><span class="p">)</span><span class="o">*</span><span class="mi">100</span><span class="p">,</span><span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[81]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>83.5</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="7.-Testing">7. Testing<a class="anchor-link" href="#7.-Testing">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">clf</span> <span class="o">=</span> <span class="n">SVC</span><span class="p">()</span>
<span class="n">clf</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">train_data</span><span class="p">,</span> <span class="n">target</span><span class="p">)</span>

<span class="n">test_data</span> <span class="o">=</span> <span class="n">test</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s2">&quot;PassengerId&quot;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
<span class="n">prediction</span> <span class="o">=</span> <span class="n">clf</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">test_data</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[84]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">submission</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span>
        <span class="s2">&quot;PassengerId&quot;</span><span class="p">:</span> <span class="n">test</span><span class="p">[</span><span class="s2">&quot;PassengerId&quot;</span><span class="p">],</span>
        <span class="s2">&quot;Survived&quot;</span><span class="p">:</span> <span class="n">prediction</span>
    <span class="p">})</span>

<span class="n">submission</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="s1">&#39;submission.csv&#39;</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[85]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">submission</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;submission.csv&#39;</span><span class="p">)</span>
<span class="n">submission</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[85]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>892</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>893</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>894</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>895</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>896</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="References">References<a class="anchor-link" href="#References">&#182;</a></h2><p>special thanks to
Minsuk Heo
this was made following along with his youtube tutorial found here:
<a href="https://www.youtube.com/watch?v=3eTSVGY_fIE">https://www.youtube.com/watch?v=3eTSVGY_fIE</a></p>

</div>
</div>
</div>
    </div>
  </div>
</body>




</html>