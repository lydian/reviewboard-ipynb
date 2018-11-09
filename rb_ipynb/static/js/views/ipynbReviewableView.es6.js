var IpynbCommentCellSelector = RB.TextCommentRowSelector.extend({
  events: {
    'click': '_onClick'
  },

  _isLineNumCell(cell) {
    return $(cell).attr('line');
  },

  _onClick(e){
    var $row = $(e.target).parents('.cell')[0];
    var lineNum = parseInt($($row).attr('line'), 10);
    this._beginLineNum = lineNum;
    this._endLineNum = lineNum;
    this._$begin = $row;
    this._$end = $row;
    this._lastSeenIndex = lineNum -1;
    $($row).addClass('selected');
    console.log('selected' + lineNum);
    this.options.reviewableView.createAndEditCommentBlock({
      beginLineNum: this._beginLineNum,
      endLineNum: this._endLineNum,
      $beginRow: this._$begin,
      $endRow: this._$end
    });
  }
});

var IpynbReviewableView = RB.TextBasedReviewableView.extend({
  className: 'ipynb-review-ui',
  events: {
    'click .cell': '_onCellClick'

  },
  commentBlockView: RB.TextBasedCommentBlockView,
  initialize() {
    RB.TextBasedReviewableView.prototype.initialize.apply(this, arguments);
    $.each($('#notebook-container .cell'), function(i, elem) {
      $(elem).attr('line', i+1);
    });
  },

  renderContent() {
    if (this.model.get('hasRenderedView')) {
      this._$renderedTable = this.$('#notebook-container');
      this._renderedSelector = new IpynbCommentCellSelector({
        el: this._$renderedTable,
        reviewableView: this
      });
      this._renderedSelector.render();
    }

  },
  _placeCommentBlockView(commentBlockView) {
    const commentBlock = commentBlockView.model;
    const beginLineNum = commentBlock.get('beginLineNum');
    const endLineNum = commentBlock.get('endLineNum');
    commentBlockView.setRows(commentBlockView.$beginRow, commentBlockView.$endRow);
    commentBlockView.$el.appendTo(
      commentBlockView.$beginRow
    );
  },
});
