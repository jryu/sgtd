function formatDate(date) {
  return [date.getMonth() + 1,
          date.getDate(),
          date.getFullYear()].join('/');
};

function createDate(y, m, d) {
  return new Date(y, m - 1, d);
};

function setLastDate(id, lastDate) {
  if (lastDate) { lastDate.setHours(0, 0, 0, 0); }

  var buttonElement = $('#btn-' + id);
  var deltaElement = $('#delta-' + id);
  if (!lastDate) {
    buttonElement.buttonMarkup({icon: 'plus'});

    deltaElement.text('New');
    deltaElement.show();
  } else if (lastDate >= TODAY) {
    buttonElement.buttonMarkup({icon: 'check'});

    deltaElement.hide();
  } else {
    buttonElement.buttonMarkup({icon: 'plus'});

    var delta = (TODAY - lastDate) / (1000 * 60 * 60 * 24);
    if (delta == 1) {
      deltaElement.text('Yesterday');
    } else {
      deltaElement.text(delta + ' days ago');
    }
    deltaElement.show();
  }
};

function toggle(todo) {
  $.mobile.loading('show');

  var isUncheck = $('#btn-' + todo).hasClass('ui-icon-check');

  var request = $.ajax(
    isUncheck ? UNCHECK_URL : CHECK_URL,
    {
      method: 'POST',
      data: {
        date: formatDate(TODAY),
        todo: todo,
      }
    });

  request.always(function() {
    $.mobile.loading('hide');
  });

  request.done(function(response) {
    var last_date;
    if (isUncheck) {
      if (response.last_date) {
        // Set date of the last log.
        last_date = createDate(response.year, response.month, response.day);
      } else {
        // There is no log on this todo item anymore.
        last_date = null;
      }
    } else {
      // The last log has been saved successfully.
      last_date = TODAY;
    }
    setLastDate(todo, last_date);
  });

  request.fail(function(response, a, b) {
    $('#errorMessage p').html(
        $.map(response.responseJSON, function(val, key) { return val; })
          .join(' '));
    $('#errorMessage').popup('open');
  });
  return false;
};
