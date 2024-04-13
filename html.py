contentHTML = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Free Tailwind CSS Status Page Template</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script
      src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.8.0/dist/alpine.min.js"
      defer
    ></script>
  <style>
  .status {
  background: linear-gradient(90.19deg, #1ee49d 0%, #19e099 100%);
  box-shadow: 0px 0px 40px rgba(27, 226, 155, 0.3);
  border-radius: 12px;
}

.container {
  margin-left: theme("margin.auto");
  margin-right: theme("margin.auto");
  max-width: 995px;
  padding: 0 theme("spacing.4");
}
/*! modern-normalize v1.0.0 | MIT License | https://github.com/sindresorhus/modern-normalize */

/*
Document
========
*/

/**
Use a better box model (opinionated).
*/

*,
*::before,
*::after {
  box-sizing: border-box;
}

/**
Use a more readable tab size (opinionated).
*/

:root {
  -moz-tab-size: 4;
  -o-tab-size: 4;
     tab-size: 4;
}

/**
1. Correct the line height in all browsers.
2. Prevent adjustments of font size after orientation changes in iOS.
*/

html {
  line-height: 1.15; /* 1 */
  -webkit-text-size-adjust: 100%; /* 2 */
}

/*
Sections
========
*/

/**
Remove the margin in all browsers.
*/

body {
  margin: 0;
}

/**
Improve consistency of default fonts in all browsers. (https://github.com/sindresorhus/modern-normalize/issues/3)
*/

body {
  font-family:
		system-ui,
		-apple-system, /* Firefox supports this but not yet `system-ui` */
		'Segoe UI',
		Roboto,
		Helvetica,
		Arial,
		sans-serif,
		'Apple Color Emoji',
		'Segoe UI Emoji';
}

/*
Grouping content
================
*/

/**
1. Add the correct height in Firefox.
2. Correct the inheritance of border color in Firefox. (https://bugzilla.mozilla.org/show_bug.cgi?id=190655)
*/

hr {
  height: 0; /* 1 */
  color: inherit; /* 2 */
}

/*
Text-level semantics
====================
*/

/**
Add the correct text decoration in Chrome, Edge, and Safari.
*/

abbr[title] {
  -webkit-text-decoration: underline dotted;
          text-decoration: underline dotted;
}

/**
Add the correct font weight in Edge and Safari.
*/

b,
strong {
  font-weight: bolder;
}

/**
1. Improve consistency of default fonts in all browsers. (https://github.com/sindresorhus/modern-normalize/issues/3)
2. Correct the odd 'em' font sizing in all browsers.
*/

code,
kbd,
samp,
pre {
  font-family:
		ui-monospace,
		SFMono-Regular,
		Consolas,
		'Liberation Mono',
		Menlo,
		monospace; /* 1 */
  font-size: 1em; /* 2 */
}

/**
Add the correct font size in all browsers.
*/

small {
  font-size: 80%;
}

/**
Prevent 'sub' and 'sup' elements from affecting the line height in all browsers.
*/

sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}

sub {
  bottom: -0.25em;
}

sup {
  top: -0.5em;
}

/*
Tabular data
============
*/

/**
1. Remove text indentation from table contents in Chrome and Safari. (https://bugs.chromium.org/p/chromium/issues/detail?id=999088, https://bugs.webkit.org/show_bug.cgi?id=201297)
2. Correct table border color inheritance in all Chrome and Safari. (https://bugs.chromium.org/p/chromium/issues/detail?id=935729, https://bugs.webkit.org/show_bug.cgi?id=195016)
*/

table {
  text-indent: 0; /* 1 */
  border-color: inherit; /* 2 */
}

/*
Forms
=====
*/

/**
1. Change the font styles in all browsers.
2. Remove the margin in Firefox and Safari.
*/

button,
input,
optgroup,
select,
textarea {
  font-family: inherit; /* 1 */
  font-size: 100%; /* 1 */
  line-height: 1.15; /* 1 */
  margin: 0; /* 2 */
}

/**
Remove the inheritance of text transform in Edge and Firefox.
1. Remove the inheritance of text transform in Firefox.
*/

button,
select { /* 1 */
  text-transform: none;
}

/**
Correct the inability to style clickable types in iOS and Safari.
*/

button,
[type='button'] {
  -webkit-appearance: button;
}

/**
Remove the inner border and padding in Firefox.
*/

/**
Restore the focus styles unset by the previous rule.
*/

/**
Remove the additional ':invalid' styles in Firefox.
See: https://github.com/mozilla/gecko-dev/blob/2f9eacd9d3d995c937b4251a5557d95d494c9be1/layout/style/res/forms.css#L728-L737
*/

/**
Remove the padding so developers are not caught out when they zero out 'fieldset' elements in all browsers.
*/

legend {
  padding: 0;
}

/**
Add the correct vertical alignment in Chrome and Firefox.
*/

progress {
  vertical-align: baseline;
}

/**
Correct the cursor style of increment and decrement buttons in Safari.
*/

/**
1. Correct the odd appearance in Chrome and Safari.
2. Correct the outline style in Safari.
*/

/**
Remove the inner padding in Chrome and Safari on macOS.
*/

/**
1. Correct the inability to style clickable types in iOS and Safari.
2. Change font properties to 'inherit' in Safari.
*/

/*
Interactive
===========
*/

/*
Add the correct display in Chrome and Safari.
*/

summary {
  display: list-item;
}

/**
 * Manually forked from SUIT CSS Base: https://github.com/suitcss/base
 * A thin layer on top of normalize.css that provides a starting point more
 * suitable for web applications.
 */

/**
 * Removes the default spacing and border for appropriate elements.
 */

blockquote,
dl,
dd,
h1,
h2,
h3,
h4,
h5,
h6,
hr,
figure,
p,
pre {
  margin: 0;
}

button {
  background-color: transparent;
  background-image: none;
}

/**
 * Work around a Firefox/IE bug where the transparent `button` background
 * results in a loss of the default `button` focus styles.
 */

button:focus {
  outline: 1px dotted;
  outline: 5px auto -webkit-focus-ring-color;
}

fieldset {
  margin: 0;
  padding: 0;
}

ol,
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

/**
 * Tailwind custom reset styles
 */

/**
 * 1. Use the user's configured `sans` font-family (with Tailwind's default
 *    sans-serif font stack as a fallback) as a sane default.
 * 2. Use Tailwind's default "normal" line-height so the user isn't forced
 *    to override it to ensure consistency even when using the default theme.
 */

html {
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"; /* 1 */
  line-height: 1.5; /* 2 */
}

/**
 * Inherit font-family and line-height from `html` so users can set them as
 * a class directly on the `html` element.
 */

body {
  font-family: inherit;
  line-height: inherit;
}

/**
 * 1. Prevent padding and border from affecting element width.
 *
 *    We used to set this in the html element and inherit from
 *    the parent element for everything else. This caused issues
 *    in shadow-dom-enhanced elements like <details> where the content
 *    is wrapped by a div with box-sizing set to `content-box`.
 *
 *    https://github.com/mozdevs/cssremedy/issues/4
 *
 *
 * 2. Allow adding a border to an element by just adding a border-width.
 *
 *    By default, the way the browser specifies that an element should have no
 *    border is by setting it's border-style to `none` in the user-agent
 *    stylesheet.
 *
 *    In order to easily add borders to elements by just setting the `border-width`
 *    property, we change the default border-style for all elements to `solid`, and
 *    use border-width to hide them instead. This way our `border` utilities only
 *    need to set the `border-width` property instead of the entire `border`
 *    shorthand, making our border utilities much more straightforward to compose.
 *
 *    https://github.com/tailwindcss/tailwindcss/pull/116
 */

*,
::before,
::after {
  box-sizing: border-box; /* 1 */
  border-width: 0; /* 2 */
  border-style: solid; /* 2 */
  border-color: #e5e7eb; /* 2 */
}

/*
 * Ensure horizontal rules are visible by default
 */

hr {
  border-top-width: 1px;
}

/**
 * Undo the `border-style: none` reset that Normalize applies to images so that
 * our `border-{width}` utilities have the expected effect.
 *
 * The Normalize reset is unnecessary for us since we default the border-width
 * to 0 on all elements.
 *
 * https://github.com/tailwindcss/tailwindcss/issues/362
 */

img {
  border-style: solid;
}

textarea {
  resize: vertical;
}

input::-moz-placeholder, textarea::-moz-placeholder {
  color: #9ca3af;
}

input:-ms-input-placeholder, textarea:-ms-input-placeholder {
  color: #9ca3af;
}

input::placeholder,
textarea::placeholder {
  color: #9ca3af;
}

button {
  cursor: pointer;
}

table {
  border-collapse: collapse;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-size: inherit;
  font-weight: inherit;
}

/**
 * Reset links to optimize for opt-in styling instead of
 * opt-out.
 */

a {
  color: inherit;
  text-decoration: inherit;
}

/**
 * Reset form element properties that are easy to forget to
 * style explicitly so you don't inadvertently introduce
 * styles that deviate from your design system. These styles
 * supplement a partial reset that is already applied by
 * normalize.css.
 */

button,
input,
optgroup,
select,
textarea {
  padding: 0;
  line-height: inherit;
  color: inherit;
}

/**
 * Use the configured 'mono' font family for elements that
 * are expected to be rendered with a monospace font, falling
 * back to the system monospace stack if there is no configured
 * 'mono' font family.
 */

pre,
code,
kbd,
samp {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

/**
 * Make replaced elements `display: block` by default as that's
 * the behavior you want almost all of the time. Inspired by
 * CSS Remedy, with `svg` added as well.
 *
 * https://github.com/mozdevs/cssremedy/issues/14
 */

img,
svg,
video,
canvas,
audio,
iframe,
embed,
object {
  display: block;
  vertical-align: middle;
}

/**
 * Constrain images and videos to the parent width and preserve
 * their instrinsic aspect ratio.
 *
 * https://github.com/mozdevs/cssremedy/issues/14
 */

img,
video {
  max-width: 100%;
  height: auto;
}

.container {
  width: 100%;
}

@media (min-width: 640px) {
  .container {
    max-width: 640px;
  }
}

@media (min-width: 768px) {
  .container {
    max-width: 768px;
  }
}

@media (min-width: 1024px) {
  .container {
    max-width: 1024px;
  }
}

@media (min-width: 1280px) {
  .container {
    max-width: 1280px;
  }
}

@media (min-width: 1536px) {
  .container {
    max-width: 1536px;
  }
}

.space-x-2 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(0.5rem * var(--tw-space-x-reverse));
  margin-left: calc(0.5rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-y-6 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(1.5rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(1.5rem * var(--tw-space-y-reverse));
}

.space-x-px > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(1px * var(--tw-space-x-reverse));
  margin-left: calc(1px * calc(1 - var(--tw-space-x-reverse)));
}

.bg-white {
  --tw-bg-opacity: 1;
  background-color: rgba(255, 255, 255, var(--tw-bg-opacity));
}

.bg-gray-100 {
  --tw-bg-opacity: 1;
  background-color: rgba(243, 244, 246, var(--tw-bg-opacity));
}

.bg-red-400 {
  --tw-bg-opacity: 1;
  background-color: rgba(248, 113, 113, var(--tw-bg-opacity));
}

.bg-yellow-400 {
  --tw-bg-opacity: 1;
  background-color: rgba(251, 191, 36, var(--tw-bg-opacity));
}

.bg-yellow-500 {
  --tw-bg-opacity: 1;
  background-color: rgba(245, 158, 11, var(--tw-bg-opacity));
}

.bg-green-400 {
  --tw-bg-opacity: 1;
  background-color: rgba(52, 211, 153, var(--tw-bg-opacity));
}

.bg-green-500 {
  --tw-bg-opacity: 1;
  background-color: rgba(16, 185, 129, var(--tw-bg-opacity));
}

.hover\:bg-gray-50:hover {
  --tw-bg-opacity: 1;
  background-color: rgba(249, 250, 251, var(--tw-bg-opacity));
}

.dark .dark\:bg-gray-800 {
  --tw-bg-opacity: 1;
  background-color: rgba(31, 41, 55, var(--tw-bg-opacity));
}

.dark .dark\:bg-dark {
  --tw-bg-opacity: 1;
  background-color: rgba(6, 7, 13, var(--tw-bg-opacity));
}

.dark .dark\:hover\:bg-gray-700:hover {
  --tw-bg-opacity: 1;
  background-color: rgba(55, 65, 81, var(--tw-bg-opacity));
}

.bg-opacity-10 {
  --tw-bg-opacity: 0.1;
}

.border-gray-300 {
  --tw-border-opacity: 1;
  border-color: rgba(209, 213, 219, var(--tw-border-opacity));
}

.dark .dark\:border-dark {
  --tw-border-opacity: 1;
  border-color: rgba(6, 7, 13, var(--tw-border-opacity));
}

.rounded {
  border-radius: 0.25rem;
}

.rounded-md {
  border-radius: 0.375rem;
}

.border {
  border-width: 1px;
}

.cursor-pointer {
  cursor: pointer;
}

.inline-block {
  display: inline-block;
}

.flex {
  display: flex;
}

.inline-flex {
  display: inline-flex;
}

.table {
  display: table;
}

.flex-col {
  flex-direction: column;
}

.items-center {
  align-items: center;
}

.justify-between {
  justify-content: space-between;
}

.flex-1 {
  flex: 1 1 0%;
}

.flex-shrink-0 {
  flex-shrink: 0;
}

.font-medium {
  font-weight: 500;
}

.font-semibold {
  font-weight: 600;
}

.font-bold {
  font-weight: 700;
}

.h-4 {
  height: 1rem;
}

.h-5 {
  height: 1.25rem;
}

.h-10 {
  height: 2.5rem;
}

.h-px {
  height: 1px;
}

.text-xs {
  font-size: 0.75rem;
  line-height: 1rem;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2rem;
}

.leading-none {
  line-height: 1;
}

.mr-1 {
  margin-right: 0.25rem;
}

.mt-2 {
  margin-top: 0.5rem;
}

.mr-2 {
  margin-right: 0.5rem;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.mt-3 {
  margin-top: 0.75rem;
}

.mb-3 {
  margin-bottom: 0.75rem;
}

.mr-4 {
  margin-right: 1rem;
}

.mt-8 {
  margin-top: 2rem;
}

.mb-8 {
  margin-bottom: 2rem;
}

.mt-12 {
  margin-top: 3rem;
}

.-ml-1 {
  margin-left: -0.25rem;
}

.-mb-px {
  margin-bottom: -1px;
}

.hover\:opacity-80:hover {
  opacity: 0.8;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.p-2 {
  padding: 0.5rem;
}

.p-5 {
  padding: 1.25rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.px-2 {
  padding-left: 0.5rem;
  padding-right: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-8 {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.py-16 {
  padding-top: 4rem;
  padding-bottom: 4rem;
}

.pb-1 {
  padding-bottom: 0.25rem;
}

.pr-2 {
  padding-right: 0.5rem;
}

.pl-2 {
  padding-left: 0.5rem;
}

* {
  --tw-shadow: 0 0 #0000;
}

.shadow-sm {
  --tw-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

* {
  --tw-ring-inset: var(--tw-empty,/*!*/ /*!*/);
  --tw-ring-offset-width: 0px;
  --tw-ring-offset-color: #fff;
  --tw-ring-color: rgba(59, 130, 246, 0.5);
  --tw-ring-offset-shadow: 0 0 #0000;
  --tw-ring-shadow: 0 0 #0000;
}

.focus\:ring-2:focus {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}

.text-black {
  --tw-text-opacity: 1;
  color: rgba(0, 0, 0, var(--tw-text-opacity));
}

.text-gray-500 {
  --tw-text-opacity: 1;
  color: rgba(107, 114, 128, var(--tw-text-opacity));
}

.text-gray-700 {
  --tw-text-opacity: 1;
  color: rgba(55, 65, 81, var(--tw-text-opacity));
}

.text-gray-800 {
  --tw-text-opacity: 1;
  color: rgba(31, 41, 55, var(--tw-text-opacity));
}

.text-gray-900 {
  --tw-text-opacity: 1;
  color: rgba(17, 24, 39, var(--tw-text-opacity));
}

.text-red-600 {
  --tw-text-opacity: 1;
  color: rgba(220, 38, 38, var(--tw-text-opacity));
}

.text-yellow-600 {
  --tw-text-opacity: 1;
  color: rgba(217, 119, 6, var(--tw-text-opacity));
}

.text-green-500 {
  --tw-text-opacity: 1;
  color: rgba(16, 185, 129, var(--tw-text-opacity));
}

.text-green-600 {
  --tw-text-opacity: 1;
  color: rgba(5, 150, 105, var(--tw-text-opacity));
}

.text-blue-700 {
  --tw-text-opacity: 1;
  color: rgba(29, 78, 216, var(--tw-text-opacity));
}

.dark .dark\:text-white {
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
}

.dark .dark\:text-gray-100 {
  --tw-text-opacity: 1;
  color: rgba(243, 244, 246, var(--tw-text-opacity));
}

.dark .dark\:text-gray-300 {
  --tw-text-opacity: 1;
  color: rgba(209, 213, 219, var(--tw-text-opacity));
}

.dark .dark\:text-gray-400 {
  --tw-text-opacity: 1;
  color: rgba(156, 163, 175, var(--tw-text-opacity));
}

.dark .dark\:text-red-400 {
  --tw-text-opacity: 1;
  color: rgba(248, 113, 113, var(--tw-text-opacity));
}

.dark .dark\:text-yellow-400 {
  --tw-text-opacity: 1;
  color: rgba(251, 191, 36, var(--tw-text-opacity));
}

.dark .dark\:text-green-400 {
  --tw-text-opacity: 1;
  color: rgba(52, 211, 153, var(--tw-text-opacity));
}

.dark .dark\:text-blue-400 {
  --tw-text-opacity: 1;
  color: rgba(96, 165, 250, var(--tw-text-opacity));
}

.uppercase {
  text-transform: uppercase;
}

.tracking-tight {
  letter-spacing: -0.025em;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.w-4 {
  width: 1rem;
}

.w-5 {
  width: 1.25rem;
}

.w-full {
  width: 100%;
}

.transform {
  --tw-translate-x: 0;
  --tw-translate-y: 0;
  --tw-rotate: 0;
  --tw-skew-x: 0;
  --tw-skew-y: 0;
  --tw-scale-x: 1;
  --tw-scale-y: 1;
  transform: translateX(var(--tw-translate-x)) translateY(var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

@-webkit-keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@-webkit-keyframes ping {
  75%, 100% {
    transform: scale(2);
    opacity: 0;
  }
}

@keyframes ping {
  75%, 100% {
    transform: scale(2);
    opacity: 0;
  }
}

@-webkit-keyframes pulse {
  50% {
    opacity: .5;
  }
}

@keyframes pulse {
  50% {
    opacity: .5;
  }
}

@-webkit-keyframes bounce {
  0%, 100% {
    transform: translateY(-25%);
    -webkit-animation-timing-function: cubic-bezier(0.8,0,1,1);
            animation-timing-function: cubic-bezier(0.8,0,1,1);
  }

  50% {
    transform: none;
    -webkit-animation-timing-function: cubic-bezier(0,0,0.2,1);
            animation-timing-function: cubic-bezier(0,0,0.2,1);
  }
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(-25%);
    -webkit-animation-timing-function: cubic-bezier(0.8,0,1,1);
            animation-timing-function: cubic-bezier(0.8,0,1,1);
  }

  50% {
    transform: none;
    -webkit-animation-timing-function: cubic-bezier(0,0,0.2,1);
            animation-timing-function: cubic-bezier(0,0,0.2,1);
  }
}

.status {
  background: linear-gradient(90.19deg, #1ee49d 0%, #19e099 100%);
  box-shadow: 0px 0px 40px rgba(27, 226, 155, 0.3);
  border-radius: 12px;
}

.container {
  margin-left: auto;
  margin-right: auto;
  max-width: 995px;
  padding: 0 1rem;
}

@media (min-width: 640px) {
}

@media (min-width: 768px) {
  .md\:flex-row {
    flex-direction: row;
  }

  .md\:mb-0 {
    margin-bottom: 0px;
  }

  .md\:mt-24 {
    margin-top: 6rem;
  }

  .md\:py-12 {
    padding-top: 3rem;
    padding-bottom: 3rem;
  }
}

@media (min-width: 1024px) {
}

@media (min-width: 1280px) {
}

@media (min-width: 1536px) {
}
  </style>
  </head>
  <body>
    <div class="dark:bg-dark">
      <header class="py-8 md:py-12 mb-8">
        <div
          class="container flex flex-col items-center md:flex-row justify-between"
        >
          <div class="logo mb-8 md:mb-0 text-gray-800 dark:text-gray-100">
            <svg
              width="197"
              height="53"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g clipPath="url(#clip0)" fill="currentColor">
                <path
                  d="M78.5552 8.04283v3.04247H75.1831V19.1032l1.672.0143 1.665.0215.0421 5.1186c.0351 4.8895.0422 5.1544.1897 5.9705.4637 2.5485 1.2856 3.9158 2.9787 4.9825 2.1286 1.3316 5.2548 1.6823 9.6104 1.0738 1.1311-.1575 2.6696-.4724 2.7399-.5512.0281-.0358-.0562-1.8112-.1827-3.9588-.1264-2.1477-.2318-4.0161-.2318-4.1593l-.007-.2577-.6815.1431c-.4707.1003-.9905.1432-1.6369.1504-.8781.0071-.9765-.0072-1.2996-.1718-.281-.1432-.3864-.2506-.5269-.5369l-.1756-.358V19.139l2.515-.0215 2.508-.0143V11.0853h-5.0582V5.00032H78.5552v3.04251zM126.256 8.04283v3.04247h-3.372V19.1032l1.672.0143 1.665.0215.042 5.1186c.035 4.8895.042 5.1544.19 5.9705.464 2.5485 1.286 3.9158 2.979 4.9825 2.128 1.3316 5.255 1.6823 9.61 1.0738 1.131-.1575 2.67-.4724 2.74-.5512.028-.0358-.056-1.8112-.183-3.9588-.126-2.1477-.231-4.0161-.231-4.1593l-.008-.2577-.681.1431c-.471.1003-.991.1432-1.637.1504-.878.0071-.976-.0072-1.299-.1718-.281-.1432-.387-.2506-.527-.5369l-.176-.358V19.139l2.515-.0215 2.508-.0143V11.0853h-5.058V5.00032H126.256v3.04251zM62.6434 10.5842c-3.0068.2577-5.4235 1.2958-7.0674 3.0568-1.2926 1.3817-1.9319 2.971-2.0092 4.9611-.0562 1.6394.2318 2.9924.8992 4.2022.4005.7302 1.4472 1.8184 2.1497 2.2336.8852.5369 2.9155 1.2743 5.5008 1.9973 2.3183.6586 3.1543 1.1741 2.8662 1.7754-.2458.5226-.9484.6443-2.4588.4224-2.1918-.315-4.6507-1.1669-6.2664-2.1691-.26-.1647-.5059-.3007-.534-.3007-.0491 0-3.6531 6.3141-3.6531 6.3928 0 .0573 1.2084.8734 1.7915 1.217 1.1521.673 2.9505 1.3602 4.4961 1.7253 2.7398.6371 6.14.7087 8.7112.179 2.9436-.6014 5.3532-2.2837 6.5616-4.5817 1.5104-2.8635.9765-6.8152-1.2084-9.0273-1.2294-1.2384-2.9435-2.1047-5.9152-2.9852-2.3324-.6944-2.6485-.8018-2.9997-.9808-.6393-.3293-.7798-.6801-.4356-1.0953.2529-.3078.6182-.3865 1.5385-.3436 1.6158.0788 3.4494.63 5.3743 1.6036.6744.3436 1.2505.63 1.2786.63.0351 0 .7025-1.3674 1.4963-3.0354 1.3348-2.8062 1.4332-3.0353 1.3208-3.1284-.3232-.2434-1.7001-.9879-2.3535-1.2671-1.9881-.8662-4.0535-1.3316-6.5826-1.4819-1.2856-.0787-1.5666-.0787-2.5009 0zM182.914 10.5842c-3.006.2577-5.423 1.2958-7.067 3.0568-1.293 1.3817-1.932 2.971-2.009 4.9611-.056 1.6394.232 2.9924.899 4.2022.401.7302 1.447 1.8184 2.15 2.2336.885.5369 2.915 1.2743 5.501 1.9973 2.318.6586 3.154 1.1741 2.866 1.7754-.246.5226-.949.6443-2.459.4224-2.192-.315-4.651-1.1669-6.266-2.1691-.26-.1647-.506-.3007-.534-.3007-.05 0-3.653 6.3141-3.653 6.3928 0 .0573 1.208.8734 1.791 1.217 1.152.673 2.951 1.3602 4.496 1.7253 2.74.6371 6.14.7087 8.711.179 2.944-.6014 5.354-2.2837 6.562-4.5817 1.51-2.8635.976-6.8152-1.208-9.0273-1.23-1.2384-2.944-2.1047-5.916-2.9852-2.332-.6944-2.648-.8018-2.999-.9808-.64-.3293-.78-.6801-.436-1.0953.253-.3078.618-.3865 1.539-.3436 1.615.0788 3.449.63 5.374 1.6036.674.3436 1.25.63 1.278.63.036 0 .703-1.3674 1.497-3.0354 1.335-2.8062 1.433-3.0353 1.32-3.1284-.323-.2434-1.7-.9879-2.353-1.2671-1.988-.8662-4.053-1.3316-6.583-1.4819-1.285-.0787-1.566-.0787-2.501 0zM106.27 10.6343c-2.41.1575-4.883.6372-7.1942 1.396-1.0327.3365-2.789 1.0166-2.9014 1.1239-.0421.0358 2.487 6.851 2.5642 6.9226.0071.0072.3934-.1718.8571-.4009 3.5193-1.7252 7.6223-2.255 9.6243-1.2384.724.3651 1.159 1.0094 1.159 1.7181v.3794h-.393c-.766 0-5.346.2148-6.14.2864-1.609.1503-3.295.587-4.5524 1.1883-2.9787 1.4103-4.4188 3.9875-4.1027 7.3092.1335 1.3602.4777 2.4913 1.0819 3.5078.3161.5298 1.1451 1.4318 1.7212 1.8685 1.686 1.2743 4.222 1.9615 6.828 1.8541 2.094-.0859 3.534-.6729 5.255-2.1405.745-.6371.668-.7015.801.673l.084.9163h10.243l-.028-7.753c-.021-6.9441-.035-7.8246-.147-8.4976-.443-2.7275-1.307-4.4957-2.986-6.0993-1.89-1.8112-4.405-2.7418-8.086-2.9924-.942-.0644-2.866-.0787-3.688-.0215zm4.25 16.7302v1.532l-.295.2649c-1.096.9521-2.979.9521-3.843 0-.309-.3436-.428-.6801-.428-1.217 0-.9378.498-1.5535 1.475-1.8255.274-.0788 2.058-.2506 2.831-.2792l.26-.0072v1.532zM144.051 19.5829c.021 5.8344.056 8.698.113 9.1132.266 2.0474.653 3.1928 1.524 4.5601 1.412 2.2193 4.215 3.422 7.679 3.2931 1.081-.0358 1.721-.1503 2.641-.4582 1.201-.4008 2.255-.995 3.253-1.8255.393-.3293.505-.3937.512-.2935.008.0716.029.5441.057 1.0595l.042.9307 5.149.0215 5.143.0143V11.0853h-10.742l-.028 7.1374c-.021 7.7029-.014 7.4738-.393 8.2756-.211.4367-.689.8662-1.11.9879-.499.1432-1.279.1074-1.686-.0787-.675-.3007-1.054-.8519-1.244-1.8112-.098-.4725-.112-1.4461-.112-7.5311v-6.9799h-10.826l.028 8.4976z"
                />
              </g>
              <rect
                y="19"
                width="10.8571"
                height="17.6429"
                rx="4"
                fill="currentColor"
              />
              <rect
                x="13.5714"
                width="10.8571"
                height="36.6429"
                rx="4"
                fill="currentColor"
              />
              <rect
                x="27.1429"
                y="12.2143"
                width="10.8571"
                height="24.4286"
                rx="4"
                fill="#1EE49D"
              />
              <path
                d="M87.3438 44h.9375c-.043-1.207-1.1563-2.1094-2.7032-2.1094-1.5312 0-2.7343.8906-2.7343 2.2344 0 1.0781.7812 1.7188 2.0312 2.0781l.9844.2813c.8437.2343 1.5937.5312 1.5937 1.3281 0 .875-.8437 1.4531-1.9531 1.4531-.9531 0-1.7969-.4219-1.875-1.3281h-1c.0938 1.3125 1.1563 2.2031 2.875 2.2031 1.8438 0 2.8906-1.0156 2.8906-2.3125 0-1.5-1.4218-1.9843-2.25-2.2031l-.8125-.2188c-.5937-.1562-1.5468-.4687-1.5468-1.3281 0-.7656.7031-1.3281 1.7656-1.3281.9687 0 1.7031.4609 1.7969 1.25zm4.629 0h-1.2813v-1.4375h-.9219V44h-.9062v.7812h.9062v3.75c0 1.0469.8438 1.5469 1.625 1.5469.3438 0 .5625-.0625.6875-.1094l-.1875-.8281c-.0781.0156-.2031.0469-.4062.0469-.4063 0-.7969-.125-.7969-.9063v-3.5h1.2813V44zm2.6573 6.1406c1.0469 0 1.5938-.5625 1.7813-.9531h.0468V50h.9219v-3.9531c0-1.9063-1.4531-2.125-2.2187-2.125-.9063 0-1.9375.3125-2.4063 1.4062l.875.3125c.2031-.4375.6836-.9062 1.5625-.9062.8477 0 1.2656.4492 1.2656 1.2187v.0313c0 .4453-.4531.4062-1.5468.5469-1.1133.1445-2.3282.3906-2.3282 1.7656 0 1.1718.9063 1.8437 2.0469 1.8437zm.1406-.8281c-.7343 0-1.2656-.3281-1.2656-.9688 0-.7031.6406-.9218 1.3594-1.0156.3906-.0469 1.4375-.1562 1.5937-.3437v.8437c0 .75-.5937 1.4844-1.6875 1.4844zM101.177 44h-1.2811v-1.4375h-.9219V44h-.9063v.7812h.9063v3.75c0 1.0469.8437 1.5469 1.625 1.5469.344 0 .562-.0625.687-.1094l-.187-.8281c-.078.0156-.203.0469-.406.0469-.407 0-.7971-.125-.7971-.9063v-3.5h1.2811V44zm4.673 3.5469c0 1.125-.859 1.6406-1.547 1.6406-.765 0-1.312-.5625-1.312-1.4375V44h-.922v3.8125c0 1.5312.812 2.2656 1.937 2.2656.907 0 1.5-.4844 1.782-1.0937h.062V50h.922v-6h-.922v3.5469zm6.365-2.2032c-.289-.8515-.937-1.4218-2.125-1.4218-1.265 0-2.203.7187-2.203 1.7343 0 .8282.492 1.3829 1.594 1.6407l1 .2343c.606.1407.891.4297.891.8438 0 .5156-.547.9375-1.407.9375-.753 0-1.226-.3242-1.39-.9688l-.875.2188c.215 1.0195 1.054 1.5625 2.281 1.5625 1.395 0 2.344-.7617 2.344-1.7969 0-.8359-.524-1.3633-1.594-1.625l-.891-.2187c-.711-.1758-1.031-.4141-1.031-.875 0-.5157.547-.8907 1.281-.8907.805 0 1.137.4454 1.297.8594l.828-.2344zM115.941 42v8h.906v-6.0781h.079l2.5 6.0781h.875l2.5-6.0781h.078V50h.906v-8h-1.156l-2.719 6.6406h-.094L117.097 42h-1.156zm11.604 8.125c1.625 0 2.719-1.2344 2.719-3.0938 0-1.875-1.094-3.1093-2.719-3.1093-1.625 0-2.719 1.2343-2.719 3.1093 0 1.8594 1.094 3.0938 2.719 3.0938zm0-.8281c-1.234 0-1.797-1.0625-1.797-2.2657 0-1.2031.563-2.2812 1.797-2.2812s1.797 1.0781 1.797 2.2812c0 1.2032-.563 2.2657-1.797 2.2657zm4.553-2.9063c0-1.0469.648-1.6406 1.531-1.6406.855 0 1.375.5586 1.375 1.5V50h.922v-3.8125c0-1.5313-.817-2.2656-2.031-2.2656-.907 0-1.469.4062-1.75 1.0156h-.079V44h-.89v6h.922v-3.6094zM137.115 50h.922v-6h-.922v6zm.469-7c.36 0 .656-.2812.656-.625 0-.3437-.296-.625-.656-.625-.359 0-.656.2813-.656.625 0 .3438.297.625.656.625zm4.256 1h-1.281v-1.4375h-.922V44h-.906v.7812h.906v3.75c0 1.0469.844 1.5469 1.625 1.5469.344 0 .563-.0625.688-.1094l-.188-.8281c-.078.0156-.203.0469-.406.0469-.406 0-.797-.125-.797-.9063v-3.5h1.281V44zm3.265 6.125c1.625 0 2.719-1.2344 2.719-3.0938 0-1.875-1.094-3.1093-2.719-3.1093-1.625 0-2.719 1.2343-2.719 3.1093 0 1.8594 1.094 3.0938 2.719 3.0938zm0-.8281c-1.234 0-1.797-1.0625-1.797-2.2657 0-1.2031.563-2.2812 1.797-2.2812s1.797 1.0781 1.797 2.2812c0 1.2032-.563 2.2657-1.797 2.2657zm3.631.7031h.922v-3.7969c0-.8125.64-1.4062 1.515-1.4062.246 0 .5.0469.563.0625v-.9375c-.106-.0078-.348-.0157-.484-.0157-.719 0-1.344.4063-1.563 1h-.062V44h-.891v6zm3.598 0h.922v-6h-.922v6zm.468-7c.36 0 .657-.2812.657-.625 0-.3437-.297-.625-.657-.625-.359 0-.656.2813-.656.625 0 .3438.297.625.656.625zm2.569 3.3906c0-1.0469.648-1.6406 1.531-1.6406.856 0 1.375.5586 1.375 1.5V50h.922v-3.8125c0-1.5313-.816-2.2656-2.031-2.2656-.906 0-1.469.4062-1.75 1.0156h-.078V44h-.891v6h.922v-3.6094zm7.439 5.9844c1.438 0 2.594-.6562 2.594-2.2031V44h-.89v.9531h-.094c-.203-.3125-.578-1.0312-1.75-1.0312-1.516 0-2.563 1.2031-2.563 3.0468 0 1.875 1.094 2.9375 2.547 2.9375 1.172 0 1.547-.6874 1.75-1.0156h.078v1.2188c0 1-.703 1.4531-1.672 1.4531-1.089 0-1.472-.5742-1.718-.9062l-.735.5156c.375.6289 1.114 1.2031 2.453 1.2031zm-.031-3.2969c-1.156 0-1.75-.875-1.75-2.125 0-1.2187.578-2.2031 1.75-2.2031 1.125 0 1.719.9062 1.719 2.2031 0 1.3281-.609 2.125-1.719 2.125z"
                fill="#a5a5a5"
              />
              <defs>
                <clipPath id="clip0">
                  <path
                    fill="#fff"
                    transform="translate(52 4.85714)"
                    d="M0 0h145v32H0z"
                  />
                </clipPath>
              </defs>
            </svg>
          </div>
          <div
            class="links flex space-x-2 items-center leading-none font-medium"
          >
            <button
              x-data="{ dark: false }"
              @click="dark = !dark; document.body.classList.toggle('dark')"
              type="button"
              class="inline-flex items-center p-2 border border-gray-300 dark:border-dark rounded-md shadow-sm text-sm font-medium text-gray-700 dark:text-gray-100 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2"
            >
              <svg
                style="display: none"
                x-show="dark"
                class="h-5 w-5"
                xmlns="http://www.w3.org/2000/svg"
                fill="currentColor"
                viewBox="0 0 24 24"
                aria-hidden="true"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
                ></path>
              </svg>
              <svg
                x-show="!dark"
                class="h-5 w-5"
                xmlns="http://www.w3.org/2000/svg"
                stroke="currentColor"
                viewBox="0 0 24 24"
                aria-hidden="true"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
                ></path>
              </svg>
            </button>
            <button
              type="button"
              class="inline-flex items-center px-4 py-2 border border-gray-300 dark:border-dark rounded-md shadow-sm text-sm font-medium text-gray-700 dark:text-gray-100 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2"
            >
              <svg
                class="-ml-1 mr-2 h-5 w-5"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 22 22"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  d="M11 15h2v2h-2v-2m0-8h2v6h-2V7m1-5C6.47 2 2 6.5 2 12a10 10 0 0 0 10 10a10 10 0 0 0 10-10A10 10 0 0 0 12 2m0 18a8 8 0 0 1-8-8a8 8 0 0 1 8-8a8 8 0 0 1 8 8a8 8 0 0 1-8 8z"
                  fill="currentColor"
                ></path>
              </svg>
              Report an Issue
            </button>
            <button
              type="button"
              class="inline-flex items-center px-4 py-2 border border-gray-300 dark:border-dark rounded-md shadow-sm text-sm font-medium text-gray-700 dark:text-gray-100 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2"
            >
              <svg
                class="-ml-1 mr-2 h-5 w-5"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  d="M10.5002 19.2498c.9625 0 1.75-.7875 1.75-1.75H8.75024c0 .9625.7875 1.75 1.74996 1.75zm5.25-5.25V9.62478c0-2.68625-1.4262-4.93499-3.9375-5.52999v-.595c0-.72625-.5862-1.3125-1.3125-1.3125-.72621 0-1.31246.58625-1.31246 1.3125v.595c-2.5025.595-3.9375 2.83499-3.9375 5.52999v4.37502l-1.75 1.75v.875H17.5002v-.875l-1.75-1.75zm-1.75.875H7.00024V9.62478c0-2.17 1.32125-3.9375 3.49996-3.9375 2.1788 0 3.5 1.7675 3.5 3.9375v5.25002zM6.63274 3.56979L5.38149 2.31854c-2.1 1.60125-3.4825 4.06874-3.605 6.86874h1.75c.06198-1.10966.37347-2.19105.91128-3.16366.53781-.9726 1.28809-1.81136 2.19497-2.45383zM17.474 9.18728h1.75c-.1313-2.8-1.5138-5.26749-3.605-6.86874l-1.2425 1.25125c.903.64563 1.6499 1.48532 2.1859 2.4574.536.97208.8475 2.05188.9116 3.16009z"
                />
              </svg>
              Subscribe
            </button>
          </div>
        </div>
        <div class="container">
          <div
            class="flex items-center p-5 mt-8 md:mt-24 status font-semibold text-dark-green"
          >
            <svg
              class="mr-4"
              width="29"
              height="29"
              fill="currentColor"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M12.3733 0c6.8363 0 12.3734 2.87113 12.3734 6.41593 0 3.5448-5.5371 6.41597-12.3734 6.41597C5.53707 12.8319 0 9.96073 0 6.41593 0 2.87113 5.53707 0 12.3733 0zM0 9.62389c0 3.54481 5.53707 6.41591 12.3733 6.41591 6.8363 0 12.3734-2.8711 12.3734-6.41591v4.94031L23.2 14.4358c-4.0059 0-7.424 2.6306-8.7232 6.3197l-2.1035.0963C5.53707 20.8518 0 17.9806 0 14.4358V9.62389zm0 8.01991c0 3.5448 5.53707 6.4159 12.3733 6.4159H13.92c0 1.6842.4176 3.2722 1.16 4.6516l-2.7067.1604C5.53707 28.8717 0 26.0006 0 22.4558v-4.812zM21.6533 29L17.4 24.1881l1.7941-1.8607 2.4592 2.5343 5.5526-5.7422L29 21.3811 21.6533 29z"
              />
            </svg>
            All Systems Operational
          </div>
        </div>
      </header>

      <main>
        <h2
          class="container text-xs tracking-wide text-gray-500 dark:text-gray-300 uppercase font-bold mb-8"
        >
          Monitors
        </h2>
        <div class="monitors space-y-6">
          <div class="monitor py-8 bg-green-400 bg-opacity-10" x-data="bars()">
            <div class="container flex items-center justify-between mb-3">
              <h3 class="text-2xl text-gray-800 dark:text-gray-100">Website</h3>
              <span class="text-green-600 dark:text-green-400 font-semibold">
                Operational
              </span>
            </div>
            <div class="container bars">
              <div class="flex space-x-px">
                <template
                  x-on:resize.window="count = calculate()"
                  x-for="i in count"
                >
                  <div
                    class="bars bg-green-400 flex-1 h-10 rounded hover:opacity-80 cursor-pointer"
                  ></div>
                </template>
              </div>
            </div>
            <div class="container mt-2">
              <div class="flex items-center">
                <span class="pr-2 flex-shrink-0 text-green-500 text-xs font-semibold" x-text="count + ' days ago'"></span>
                <div class="h-px bg-green-500 w-full"></div>
                <span class="px-2 flex-shrink-0 text-green-500 text-xs font-semibold">99.8%</span>
                <div class="h-px bg-green-500 w-full"></div>
                <span class="pl-2 flex-shrink-0 text-green-500 text-xs font-semibold">Today</span>
              </div>
            </div>
          </div>
          <div class="monitor py-8 bg-yellow-500 bg-opacity-10">
            <div class="container flex items-center justify-between mb-3">
              <h3 class="text-2xl text-gray-800 dark:text-gray-100">API</h3>
              <span class="text-yellow-600 dark:text-yellow-400 font-semibold">
                Degraded Performance
              </span>
            </div>
            <div class="container bars">
              <div class="flex space-x-px">
                <template
                  x-data="bars()"
                  x-on:resize.window="count = calculate()"
                  x-for="i in count"
                >
                  <div
                    class="bars bg-yellow-400 flex-1 h-10 rounded hover:opacity-80 cursor-pointer"
                  ></div>
                </template>
              </div>
            </div>
          </div>
          <div class="monitor py-8 bg-red-400 bg-opacity-10">
            <div class="container flex items-center justify-between mb-3">
              <h3 class="text-2xl text-gray-800 dark:text-gray-100">
                Webhooks
              </h3>
              <span class="text-red-600 dark:text-red-400 font-semibold">
                Major Outage
              </span>
            </div>
            <div class="container bars">
              <div class="flex space-x-px">
                <template
                  x-data="bars()"
                  x-on:resize.window="count = calculate()"
                  x-for="i in count"
                >
                  <div
                    class="bars bg-red-400 flex-1 h-10 rounded hover:opacity-80 cursor-pointer"
                  ></div>
                </template>
              </div>
            </div>
          </div>
        </div>
  
      </main>

      <footer class="py-16 text-gray-700 dark:text-gray-100 bg-gray-100 dark:bg-gray-800">
        <div class="container flex justify-between">
          <a href="#" class="flex items-center">
            <svg
              class="h-4 w-4 mr-1 -mb-px"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 256 256"
              aria-hidden="true"
            >
              <path d="M224 128a8 8 0 0 1-8 8H59.314l58.343 58.343a8 8 0 0 1-11.314 11.314l-72-72a8 8 0 0 1 0-11.314l72-72a8 8 0 0 1 11.314 11.314L59.314 120H216a8 8 0 0 1 8 8z" fill="currentColor"></path>
            </svg>
            Incident history
          </a>
          <div>
            Powered by
            <span class="font-semibold text-black dark:text-white">Status</span>
          </div>
        </div>
      </footer>
    </div>
    <script>
      function bars() {
        const calculate = () =>
          Math.min(Math.floor(window.innerWidth / 10.7), 90);
        return {
          count: calculate(),
          calculate,
        };
      }
    </script>
  </body>
</html>


"""
