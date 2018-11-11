# Reviewboard Extension for review jupyter notebook

- This extension renders jupyter notebook so that it is easier to code review jupyter notebook.
- The extension use nbconvert locally for render, there's no need to convert the notebook to different format by yourself.
- The template kept the javascript definition, namely, if your jupyter notebook is using external library (plotly, MathJax), it will still show it for you.


## Limitiation:
- Due to the limitation of reviewboard plugin, this only render the file attachement

## TODO:
- Add tests
- Better support for diff (probably use nbdime) instead of the current built-in differ.


## Screenshot:
- render ipynb
![Render Ipynb](/screenshots/render_notebook.png?raw=true "Render Ipynb")
- comment 
![Comment](/screenshots/comment.png?raw=true "Comment")
- diff
![diff](/screenshots/diff.png?raw=true "diff")
