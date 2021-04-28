/*
	Massively by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function ($) {

	var $window = $(window),
		$body = $('body'),
		$wrapper = $('#wrapper'),
		$header = $('#header'),
		$nav = $('#nav'),
		$main = $('#main'),
		$navPanelToggle, $navPanel, $navPanelInner;

	// Breakpoints.
	breakpoints({
		default: ['1681px', null],
		xlarge: ['1281px', '1680px'],
		large: ['981px', '1280px'],
		medium: ['737px', '980px'],
		small: ['481px', '736px'],
		xsmall: ['361px', '480px'],
		xxsmall: [null, '360px']
	});

	/**
	 * Applies parallax scrolling to an element's background image.
	 * @return {jQuery} jQuery object.
	 */
	$.fn._parallax = function (intensity) {

		var $window = $(window),
			$this = $(this);

		if (this.length == 0 || intensity === 0)
			return $this;

		if (this.length > 1) {

			for (var i = 0; i < this.length; i++)
				$(this[i])._parallax(intensity);

			return $this;

		}

		if (!intensity)
			intensity = 0.25;

		$this.each(function () {

			var $t = $(this),
				$bg = $('<div class="bg"></div>').appendTo($t),
				on, off;

			on = function () {

				$bg
					.removeClass('fixed')
					.css('transform', 'matrix(1,0,0,1,0,0)');

				$window
					.on('scroll._parallax', function () {

						var pos = parseInt($window.scrollTop()) - parseInt($t.position().top);

						$bg.css('transform', 'matrix(1,0,0,1,0,' + (pos * intensity) + ')');

					});

			};

			off = function () {

				$bg
					.addClass('fixed')
					.css('transform', 'none');

				$window
					.off('scroll._parallax');

			};

			// Disable parallax on ..
			if (browser.name == 'ie' // IE
				||
				browser.name == 'edge' // Edge
				||
				window.devicePixelRatio > 1 // Retina/HiDPI (= poor performance)
				||
				browser.mobile) // Mobile devices
				off();

			// Enable everywhere else.
			else {

				breakpoints.on('>large', on);
				breakpoints.on('<=large', off);

			}

		});

		$window
			.off('load._parallax resize._parallax')
			.on('load._parallax resize._parallax', function () {
				$window.trigger('scroll');
			});

		return $(this);

	};

	// Play initial animations on page load.
	$window.on('load', function () {
		window.setTimeout(function () {
			$body.removeClass('is-preload');
		}, 100);
	});

	// Scrolly.
	$('.scrolly').scrolly();

	// Background.
	$wrapper._parallax(0.925);

	// Nav Panel.

	// Toggle.
	$navPanelToggle = $(
			'<a href="#navPanel" id="navPanelToggle">Menu</a>'
		)
		.appendTo($wrapper);

	// Change toggle styling once we've scrolled past the header.
	$header.scrollex({
		bottom: '5vh',
		enter: function () {
			$navPanelToggle.removeClass('alt');
		},
		leave: function () {
			$navPanelToggle.addClass('alt');
		}
	});

	// Panel.
	$navPanel = $(
			'<div id="navPanel">' +
			'<nav>' +
			'</nav>' +
			'<a href="#navPanel" class="close"></a>' +
			'</div>'
		)
		.appendTo($body)
		.panel({
			delay: 500,
			hideOnClick: true,
			hideOnSwipe: true,
			resetScroll: true,
			resetForms: true,
			side: 'right',
			target: $body,
			visibleClass: 'is-navPanel-visible'
		});

	// Get inner.
	$navPanelInner = $navPanel.children('nav');

	// Move nav content on breakpoint change.
	var $navContent = $nav.children();

	breakpoints.on('>medium', function () {

		// NavPanel -> Nav.
		$navContent.appendTo($nav);

		// Flip icon classes.
		$nav.find('.icons, .icon')
			.removeClass('alt');

	});

	breakpoints.on('<=medium', function () {

		// Nav -> NavPanel.
		$navContent.appendTo($navPanelInner);

		// Flip icon classes.
		$navPanelInner.find('.icons, .icon')
			.addClass('alt');

	});

	// Hack: Disable transitions on WP.
	if (browser.os == 'wp' &&
		browser.osVersion < 10)
		$navPanel
		.css('transition', 'none');

	// Intro.
	var $intro = $('#intro');

	if ($intro.length > 0) {

		// Hack: Fix flex min-height on IE.
		if (browser.name == 'ie') {
			$window.on('resize.ie-intro-fix', function () {

				var h = $intro.height();

				if (h > $window.height())
					$intro.css('height', 'auto');
				else
					$intro.css('height', h);

			}).trigger('resize.ie-intro-fix');
		}

		// Hide intro on scroll (> small).
		breakpoints.on('>small', function () {

			$main.unscrollex();

			$main.scrollex({
				mode: 'bottom',
				top: '25vh',
				bottom: '-50vh',
				enter: function () {
					$intro.addClass('hidden');
				},
				leave: function () {
					$intro.removeClass('hidden');
				}
			});

		});

		// Hide intro on scroll (<= small).
		breakpoints.on('<=small', function () {

			$main.unscrollex();

			$main.scrollex({
				mode: 'middle',
				top: '15vh',
				bottom: '-15vh',
				enter: function () {
					$intro.addClass('hidden');
				},
				leave: function () {
					$intro.removeClass('hidden');
				}
			});

		});

	}
	const inputField = document.querySelector('.chosen-value');
	const dropdown = document.querySelector('.value-list');
	const dropdownArray = [...document.querySelectorAll('.nomFournisseur')];
	let valueArray = [];
	dropdownArray.forEach(item => {
		valueArray.push(item.textContent);
	});


	inputField.addEventListener('input', () => {
		dropdown.classList.add('open');
		let inputValue = inputField.value;
		if (inputValue.length > 0) {
			for (let j = 0; j < valueArray.length; j++) {
				if (!(inputValue.substring(0, inputValue.length) === valueArray[j].substring(0, inputValue.length))) {
					dropdownArray[j].classList.add('closed');
				} else {
					dropdownArray[j].classList.remove('closed');
				}
			}
		} else {
			for (let i = 0; i < dropdownArray.length; i++) {
				dropdownArray[i].classList.remove('closed');
			}
		}
	});

	dropdownArray.forEach(item => {
		item.addEventListener('click', (evt) => {
			inputField.value = item.textContent;
			$('#filtrer').val(inputField.value)
			if (null == null) {
				data = JSON.parse($("#data").val());
			}
			if (target === '#changeId') {
				content = ` <div id="codes" class='lignes'>
                        <div id="` + $(target).val() + `"  class="grid-item code" 
                        onclick="divClicked('` + $(target).val() + `')">` +
					$(target).val() + `
                        </div></div>`
				$(id).replaceWith(content)
			} else {
				$(id).val(data[field1][data[filed2].indexOf($(target).val())])
			}

			dropdownArray.forEach(dropdown => {
				dropdown.classList.add('closed');
			});
		});
	})

	inputField.addEventListener('focus', () => {
		inputField.placeholder = 'Type to filter';
		inputField.value = ""
		dropdown.classList.add('open');
		dropdownArray.forEach(dropdown => {
			dropdown.classList.remove('closed');
		});
	});

	inputField.addEventListener('blur', () => {
		inputField.placeholder = 'Select state';
		dropdown.classList.remove('open');
	});

	document.addEventListener('click', (evt) => {
		const isDropdown = dropdown.contains(evt.target);
		const isInput = inputField.contains(evt.target);
		if (!isDropdown && !isInput) {
			dropdown.classList.remove('open');
		}
	});

})(jQuery);