# pelican-uglify-plugin

Pelican plugin to use [uglify-es](https://www.npmjs.com/package/uglify-es)/ [uglifycss](https://www.npmjs.com/package/uglifycss) for assets. The code is strongly inspired by [Pelican Yuicompressor Plugin](https://github.com/auroredea/yuicompressor).

## Installation

You need a working [npm](https://www.npmjs.com/) installation.

After installing npm execute:

```bash
npm install -g uglifycss
npm install -g uglify-es
```

## Usage

You will need to place the `uglify.py` in your `plugins/` folder and add `uglify` to your `PLUGINS = ['yuicompressor']` config.

The Plugin minifies all css and js files. This may add a lot of processing when making content. Excluded are files ending either `.min.js` or `.min.css`. The plugin *alters* the names of `js`/ `css` files from `name.js` and `name.css` to `name.min.js` and `name.min.css`. Keep this in mind when importing your `css` and `js` files.

You can change the `UGLIFYJS_EXECUTABLE` and `UGLIFYCSS_EXECUTABLE` arcording to your needs if needed. The defaults are `UGLIFYJS_EXECUTABLE=uglifyjs` and `UGLIFYCSS_EXECUTABLE=uglifycss`. You may also pass options (such as `-c`) after the uglifycss/ -js executable with `UGLIFYJS_OPTIONS=[your options]` (defualt = \["-c", "--source-map"\]) and `UGLIFYCSS_OPTIONS=[your options]` (the options need to be iterable, e.g. list or set).

As a tool for excluding content that should not be minified the `UGLIFY_EXCLUDE` option is avalaible and should be provided as a list of [regular expressions](https://docs.python.org/3/howto/regex.html).

## License and Maintainer

This Project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2020 Cobalt <chaosthe0rie@pm.me>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
