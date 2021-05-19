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




	$("body").on("keyup", '.qte', function () {
		var lenData = parseInt($('#lenData').val())
		var mht = 0
		var tva = 0
		var ttc = 0
		var num = ($(this)[0].id).substr(($(this)[0].id).length - 1)

		if ($('#quantite-' + num).val().length > 0 && $('#quantite-' + num).val() !== '0') {
			console.log("sheeesh")
			var montant = (parseInt($('#quantite-' + num).val()) * parseInt($('#prix_unitaire-' + num).val())).toString()
			$('#mantant-' + num).val(montant)
		} else {
			console.log("not sheees")
			$('#mantant-' + num).val('0')
		}

		for (var i = 1; i <= lenData; i++) {
			console.log(i)
			console.log($('#mantant-' + i).val())
			mht = mht + parseInt($('#mantant-' + i).val())
			console.log(mht)

		}
		$('#MHT').val(mht.toString())

		tva = (mht * 19) / 100
		$('#TVA').val(tva.toString())
		ttc = tva + mht
		$('#TTC').val(ttc.toString())


	})
	var lista = []

	try {
		var $eventSelect2 = $("#selectjs-1-2")
		$eventSelect2.select2({
			placeholder: "Type",
			ajax: {
				type: "GET",

				dataType: 'json',
				url: function (params) {
					var num = $(this)["context"].id
					var whiche = num.substring(num.length - 1)
					return 'loadMore/' + params.term + "/" + whiche;
				},

				processResults: function (data) {
					// console.log(data)
					lista = []
					for (d in data) {
						lista.push(data[d])
					}
					// console.log(lista)
					var fin = []
					fin = data

					return {


						results: $.map(fin, function (item) {
								// console.log(item)

								$eventSelect2.on("select2:select", function (e) {
									nom = e.params.data.id
									valeur = e.params.data.text
									var $newOption = $("<option selected='selected'></option>").val(valeur).text(nom)

									$("#selectjs-1-1").append($newOption).trigger('change');
								})

								return {
									text: item.id_article,
									id: item.nom_article

								}

							}

						)

					}



				},
				cache: true,


			}
		})
	} catch (error) {
		console.log('not here')
	}


	try {
		var $eventSelect = $("#selectjs-1-1")
		$eventSelect.select2({
			placeholder: "Type",
			ajax: {
				type: "GET",

				dataType: 'json',
				url: function (params) {
					var num = $(this)["context"].id
					var whiche = num.substring(num.length - 1)
					return 'loadMore/' + params.term + "/" + whiche;
				},

				processResults: function (data) {
					// console.log(data)
					lista = []
					for (d in data) {
						lista.push(data[d])
					}
					// console.log(lista)
					var fin = []
					fin = data





					return {


						results: $.map(fin, function (item) {
							$eventSelect.on("select2:select", function (e) {
								id = e.params.data.id
								var $newOption = $("<option selected='selected'></option>").val(id).text(id)

								$("#selectjs-1-2").append($newOption).trigger('change');
							})
							// console.log(item.nom_article)


							return {
								text: item.nom_article,
								id: item.id_article

							}
						})

					}



				},
				cache: true,


			}
		})

	} catch (error) {
		console.log('not here')
	}

	try {
		var $selectDistri = $("#selectDistri")
		$selectDistri.select2({
			placeholder: "Type",
			ajax: {
				type: "GET",
				dataType: 'json',
				url: function (params) {

					return 'loadMore/' + params.term
				},

				processResults: function (data) {
					// console.log(data)
					lista = []
					for (d in data) {
						lista.push(data[d])
					}
					// console.log(lista)
					var fin = []
					fin = data





					return {


						results: $.map(fin, function (item) {

							return {
								text: item.nom_ditributeur,
								id: item.id_ditributeur

							}
						})

					}



				},
				cache: true,


			}
		})
	} catch (error) {
		console.log('not here')
	}



	function closeSelect(idContainer, e, that) {
		var num = (that.parents()[2].id)
		num = (num.substr(num.length - 1))
		var pos = lista.map(function (event) {
			console.log(event)
			if (idContainer === "#select2-selectjs-1-1-container") {
				return event.nom_article
			} else {
				return event.id_article
			}



		}).indexOf($(idContainer).text());

		$('#unitedemeusur-' + num).val(lista[pos]['unite_mesure'])
		console.log(lista[pos]['prix_unitaire'])
		console.log('#prix_unitaire-' + num)
		$('#prix_unitaire-' + num).val(lista[pos]['prix_unitaire'])

		console.log("select2:close", e);
	}


	$eventSelect.on("select2:close", function (e) {
		closeSelect("#select2-selectjs-1-1-container", e, $(this))
	})
	$eventSelect2.on("select2:close", function (e) {
		closeSelect("#select2-selectjs-1-2-container", e, $(this))
	})



})(jQuery);