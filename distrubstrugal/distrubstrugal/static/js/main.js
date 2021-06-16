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

	function replaceTableSuiviContract() {
		$('#select2-selectDistri-container').text('')
		var dateE = $('#dateE').val()
		dateE.length <= 0 ? dateE = 'None' : dateE = dateE


		$.ajax({
			type: 'GET',
			url: `filterer/None/${dateE}`,
			success: function (data) {
				console.log(data)
				var table = $('#table-div').children()
				new_content = `<div id='suivi_des_contrat' class="table-wrapper">
				<table class="alt">
					<thead>
						<tr>
							<th>Client</th>
							<th>Date Effet</th>
							<th>Date Fin de Contrat</th>
						</tr>
					</thead>
					<tbody>`
				for (d in data['result']) {

					new_content = new_content + `<tr>
								<td id = ` + data['result'][d]['id'] + ` hidden></td>
								<td>` + data['result'][d]['nom'] + `</td>
								<td>` + data['result'][d]['date_effet'] + `</td>
								<td>` + data['result'][d]['date_echeance'] + `</td>
								<td><button
								  id="{{com.id}}"
								  onClick=showDetail(this.id)
								  type="button"
								  class="btn "
								  data-toggle="modal" data-target="#exampleModal"
								>Detail</button></td>
								
								
							</tr>`
				}
				new_content = new_content +
					`
						</tbody>
					</table>
				  </div>`
				table.replaceWith(new_content)

			},
			error: function (response) {
				console.log(response)
			}
		})
	}

	function initiamizeVoutsrapTable(params) {
		var $table = $('#bootstrap-table');
		$table.bootstrapTable({
			toolbar: ".toolbar",
			clickToSelect: true,
			showRefresh: false,
			search: true,
			showToggle: false,
			showColumns: false,
			pagination: true,
			searchAlign: 'left',
			pageSize: 8,
			clickToSelect: false,
			// pageList: [8,10,25,50,100],

			formatShowingRows: function (pageFrom, pageTo, totalRows) {
				//do nothing here, we don't want to show the text "showing x of y from..."
			},
			formatRecordsPerPage: function (pageNumber) {
				return pageNumber + " rows visible";
			},
			icons: {
				refresh: 'fa fa-refresh',
				toggle: 'fa fa-th-list',
				columns: 'fa fa-columns',
				detailOpen: 'fa fa-plus-circle',
				detailClose: 'ti-close'
			}
		});

		//activate the tooltips after the data table is initialized
		$('[rel="tooltip"]').tooltip();

		$(window).resize(function () {
			$table.bootstrapTable('resetView');
		});
	}

	function replaceTableListeCommande() {
		var dateE = $('#dateE').val()
		var dist = $('#select2-selectDistri-container').text()
		var etat = $("#etat").val();
		var refdes = $('#select2-refdes-container').text()
		dist.length <= 0 ? dist = 'None' : dist = dist
		etat.length <= 0 ? etat = 'None' : etat = etat
		if (refdes.length > 0) {
			refdes = refdes.replace('/', '-')
		}
		refdes.length <= 0 ? refdes = 'None' : refdes = refdes
		$.ajax({
			type: 'GET',
			url: `filtererListCommand/${dist}/${dateE}/${etat}/${refdes}`,
			success: function (data) {
				var origin = window.location.origin;
				buildTable(data, origin, 1)

			},
			error: function (response) {
				console.log(response)
			}
		})
	}

	function replaceTablelistCommandesD() {
		var dateE = $('#dateE').val()
		var etat = $("#etat").val();

		etat.length <= 0 ? etat = 'None' : etat = etat

		$.ajax({
			type: 'GET',
			url: `filterer/${etat}/${dateE}`,
			success: function (data) {
				var origin = window.location.origin;
				console.log(data)
				var table = $('#table-div-commande').children()
				new_content = `<div id='table-div-commande' class="table-wrapper">
				<table class="alt">
					<thead>
					<tr>
                    <th>Ref Description</th>
                    <th>Date</th>
                    <th>THT</th>
                    <th>TTC</th>
                    <th>Etat</th>
                	</tr>
					</thead>
					<tbody>`
				for (d in data['result']) {

					new_content = new_content + `<tr>
								<td id = ` + data['result'][d]['id'] + ` hidden></td>
								<td>` + data['result'][d]['reference_description'] + `</td>
								<td>` + data['result'][d]['date'] + `</td>
								<td>` + data['result'][d]['totaleHT'] + `</td>
								<td>` + data['result'][d]['totaleTTC'] + `</td>
								<td>` + data['result'][d]['etat'] + `</td>
								<td><button
								  id="` + data['result'][d]['id'] + `"
								  onClick=showDetail(this.id)
								  type="button"
								  class="btn "
								  data-toggle="modal" data-target="#exampleModal"
								>Detail</button></td>

								<td>
								<a
								id="` + data['result'][d]['id'] + `"
								onClick=showDetail(this.id)
								type="button"
								class="btn "
								href="` + origin + `/distributeur/pdf_view/` + data['result'][d]['id'] + `"
								target="_blank"
							  >Imprimer</a>
							  </td>
				
							</tr>`
				}
				new_content = new_content + `
		
						</tbody>
					</table>
				  </div>`
				table.replaceWith(new_content)

			},
			error: function (response) {
				console.log(response)
			}
		})
	}

	function changeTableListCommandeWithEtat(params) {
		var dateE = $('#dateE').val()
		var dist = $('#select2-selectDistri-container').text()
		var etat = $("#etat").val();
		var refdes = $('#select2-refdes-container').text()
		dateE.length <= 0 ? dateE = 'None' : dateE = dateE
		if (refdes.length > 0) {
			refdes = refdes.replace('/', '-')
		}
		refdes.length <= 0 ? refdes = 'None' : refdes = refdes
		$.ajax({
			type: 'GET',
			url: `filtererListCommand/${dist}/${dateE}/${etat}/${refdes}`,
			success: function (data) {
				var origin = window.location.origin;
				buildTable(data, origin, 1)

			},
			error: function (response) {
				console.log(response)
			}
		})
	}

	function changeTableListCommandeDWithEtat(params) {
		var dateE = $('#dateE').val()

		var etat = $("#etat").val();

		dateE.length <= 0 ? dateE = 'None' : dateE = dateE


		$.ajax({
			type: 'GET',
			url: `filterer/${etat}/${dateE}`,
			success: function (data) {
				var origin = window.location.origin;
				buildTable(data, origin, 1)

			},
			error: function (response) {
				console.log(response)
			}
		})
	}

	$('body').on('change', '#dateE', function () {
		var pathname = window.location.pathname

		if (pathname.includes('distributeur')) {
			replaceTablelistCommandesD()
		} else if (pathname.includes('suiviContrat')) {
			replaceTableSuiviContract()
		} else {
			replaceTableListeCommande()
		}

	})

	function intspace(params) {
		if (params.toString().indexOf('.') === -1) {
			return params.toLocaleString()
		} else {

			params = params.toLocaleString()
			return params
		}
	}

	$("body").on("keyup", '.qte', function () {
		var lenData = parseInt($('#lenData').val())
		var mht = 0
		var tva = 0
		var ttc = 0
		var num = ($(this)[0].id).substr(($(this)[0].id).length - 1)

		if ($('#quantite-' + num).val().length > 0 && $('#quantite-' + num).val() !== '0') {

			var montant = (parseInt($('#quantite-' + num).val()) * parseInt($('#prix_unitaire-' + num).val()))
			console.log(intspace(montant))

			$('#mantant-' + num).val(montant.toString())
			$('#mantant-' + num + "-forshow").val(intspace(montant))
		} else {

			$('#mantant-' + num).val('0')
		}


		for (var i = 1; i <= lenData; i++) {

			mht = mht + parseInt($('#mantant-' + i).val())

		}



		$('#MHT').val(mht)
		$('#MHT-forshow').val(intspace(mht))

		tva = (mht * 19) / 100

		$('#TVA').val(tva)
		$('#TVA-forshow').val(intspace(tva))
		ttc = tva + mht

		$('#TTC').val(ttc)
		$('#TTC-forshow').val(intspace(ttc))


	})


	$('#etat').on('change', function () {
		var pathname = window.location.pathname

		if (pathname.includes('distributeur')) {
			changeTableListCommandeDWithEtat()
		} else {

			changeTableListCommandeWithEtat()
		}


	});

	var lista = []
	//Message fade out
	try {
		setTimeout(function () {
			jQuery("#message").fadeOut("slow");
		}, 3000);
	} catch (error) {
		return;
	}
	var pathname = window.location.pathname
	if (!pathname.includes('modifier')) {

		//eventSelect2
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
						var pathname = window.location.pathname;
						pathname === '/' ? loca = 'distributeur/loadMore/' + params.term + "/" + whiche :
							loca = 'loadMore/' + params.term + "/" + whiche
						return loca
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

		// eventSelect
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
						var pathname = window.location.pathname;
						pathname === '/' ? loca = 'distributeur/loadMore/' + params.term + "/" + whiche :
							loca = 'loadMore/' + params.term + "/" + whiche
						return loca
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

		$eventSelect.on("select2:close", function (e) {
			closeSelect("#select2-selectjs-1-1-container", e, $(this))
		})

		$eventSelect2.on("select2:close", function (e) {
			closeSelect("#select2-selectjs-1-2-container", e, $(this))
		})
	}
	//selectDistri
	try {
		var $selectDistri = $("#selectDistri")
		$selectDistri.select2({
			placeholder: "Recherche Ditributeur",
			ajax: {
				type: "GET",
				dataType: 'json',
				url: function (params) {
					var whicheone = 'dist'
					return 'loadMoreD/' + params.term + '/' + whicheone
				},

				processResults: function (data) {
					lista = []
					for (d in data) {
						lista.push(data[d])
					}
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
		console.log(error)
	}



	//selectrefDes
	try {
		var $selectRefDesc = $("#refdes")
		$selectRefDesc.select2({
			placeholder: "Recherche par Ref Des",
			ajax: {
				type: "GET",
				dataType: 'json',
				url: function (params) {
					var whicheone = 'refDes'
					return 'loadMoreD/' + params.term + '/' + whicheone
				},

				processResults: function (data) {
					console.log(data)
					lista = []
					for (d in data) {
						lista.push(data[d])
					}
					var fin = []
					fin = data
					return {
						results: $.map(fin, function (item) {
							return {
								text: item.reference_description,
								id: item.id_commande
							}
						})
					}
				},
				cache: true,
			}
		})
	} catch (error) {
		console.log(error)
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

	function changeTableSuivi() {
		var nom_distri = $('#select2-selectDistri-container').text()
		console.log(nom_distri)
		var dateE = $('#dateE').val()
		dateE.length <= 0 ? dateE = 'None' : dateE = dateE

		$.ajax({
			type: 'GET',
			url: `filterer/${nom_distri}/${dateE}`,
			success: function (data) {
				console.log("data" + data['result'])


				var table = $('#table-div').children()
				console.log(dateE)
				console.log(dateE.length)
				if (dateE === 'None') {
					console.log("rani fel if te3 else")
					new_content = `<div id='suivi_des_contrat' class="table-wrapper">
					<table class="alt">
						<thead>
							<tr>
								<th>Client</th>
								<th>Date Effet</th>
								<th>Date Fin de Contrat</th>
							</tr>
						</thead>
						<tbody>
					<tr>
								<td id = ` + data['id'] + ` hidden></td>
								<td>` + data['nom'] + `</td>
								<td>` + data['date_effet'] + `</td>
								<td>` + data['date_echeance'] + `</td>
								<td><button
								  id="` + data['id'] + `"
								  onClick=showDetail(` + data['id'] + `)
								  type="button"
								  class="btn "
								  data-toggle="modal" data-target="#exampleModal"
								>Detail</button></td>
	
							</tr>
						</tbody>
					</table>
				  </div>`
					table.replaceWith(new_content)
				} else {

					console.log("rani fel else te3 else")

					if (data && !jQuery.isEmptyObject((data['result'])) && data.constructor === Object) {
						console.log('rani fel if te3 else te3 else')
						new_content = `<div id='suivi_des_contrat' class="table-wrapper">
						<table class="alt">
							<thead>
								<tr>
									<th>Client</th>
									<th>Date Effet</th>
									<th>Date Fin de Contrat</th>
								</tr>
							</thead>
							<tbody>
						<tr>
									<td id = ` + data['result']['id'] + ` hidden></td>
									<td>` + data['result']['nom'] + `</td>
									<td>` + data['result']['date_effet'] + `</td>
									<td>` + data['result']['date_echeance'] + `</td>
									<td><button
									  id="` + data['result']['id'] + `"
									  onClick=showDetail(` + data['result']['id'] + `)
									  type="button"
									  class="btn "
									  data-toggle="modal" data-target="#exampleModal"
									>Detail</button></td>
		
								</tr>
							</tbody>
						</table>
					  </div>`
						table.replaceWith(new_content)
					} else {
						new_content = `<div id='suivi_des_contrat' class="table-wrapper">
					<table class="alt">
						<thead>
							<tr>
								<th>Client</th>
								<th>Date Effet</th>
								<th>Date Fin de Contrat</th>
							</tr>
						</thead>
						<tbody></tbody></table></div>
						`
						table.replaceWith(new_content)
					}
				}






			},
			error: function (response) {
				console.log(response)
			}

		})
	}

	function changeTableListCommande() {
		var dateE = $('#dateE').val()
		var dist = $('#select2-selectDistri-container').text()
		var etat = $("#etat").val();
		var refdes = $('#select2-refdes-container').text()
		dateE.length <= 0 ? dateE = 'None' : dateE = dateE
		etat.length <= 0 ? etat = 'None' : etat = etat
		if (refdes.length > 0) {
			refdes = refdes.replace('/', '-')
		}
		console.log(etat)
		refdes.length <= 0 ? refdes = 'None' : refdes = refdes
		$.ajax({
			type: 'GET',
			url: `filtererListCommand/${dist}/${dateE}/${etat}/${refdes}`,
			success: function (data) {



				var origin = window.location.origin;
				console.log(data)
				buildTable(data, origin, 1)

			},
			error: function (response) {
				console.log(response)
			}
		})
	}

	function displaySold() {
		var id_disri = parseInt($('#selectDistri')[0][1]['value'])
		// sum(account_move_line.credit)
		// ,sum(account_move_line.debit)
		// ,sum(account_move_line.debit  - account_move_line.credit)
		$.ajax({
			url: `http://10.10.10.64:8585/diststru/sold/?id_dist=${id_disri}`,
			type: 'POST',
			success: function (data) {
				console.log("data " + data[0][0])
				infoSold = document.getElementById('info-sold')
				infoSold.innerHTML = ''

				infoSold.innerHTML = `<div style="
											display: flex;
											flex-direction: column;
											align-items: center;
											justify-content: space-between;
										">
										<label>Client</label><input type="text" value="${data[0][0]}" readonly>
										<label>Credit</label><input type="text" value="${data[0][1]}" readonly>
										<label>Debit</label><input type="text" value="${data[0][2]}" readonly>	
										<label>Sold</label><input type="text" value="${data[0][3]}" readonly>	
										</div>
										<hr>`

			},
			error: function (response) {
				console.log(response)
			}
		})
	}

	$selectDistri.on("select2:close", function (e) {
		var pathname = window.location.pathname;
		if (pathname.includes('suiviContrat')) {
			changeTableSuivi()
		} else if (pathname.includes('soldClient')) {
			displaySold()
		} else {
			changeTableListCommande()
		}
	})


	$selectRefDesc.on("select2:close", function (e) {
		var refDesc = e.params.originalSelect2Event.data['text']

		refdes = refDesc.replace('/', '-')
		$.ajax({
			type: 'GET',
			url: `filtererListCommand/None/None/None/${refdes}`,
			success: function (data) {
				var origin = window.location.origin;
				buildTable(data, origin, 1)


			},
			error: function (response) {
				console.log(response)
			}

		})
	})


	function paginator(result, page, rows) {
		var i = ""
		var querset = []
		for (i in Object.keys(result)) {
			querset.push(result[i])
		}
		console.log(querset)
		var trimStart = (page - 1) * rows
		var trimEnd = trimStart + rows
		var trimedData = querset.slice(trimStart, trimEnd)
		var pages = Math.ceil(querset.length / rows)

		return {
			'result': trimedData,
			'pages': pages
		}
	}

	function pageButtons(pages, data, numPage, champ) {
		var origin = window.location.origin;
		var wrapper = document.getElementById('pagination-wrapper')
		wrapper.innerHTML = ""
		var mexLeft = (numPage - Math.floor(champ / 2))
		var maxRight = (numPage + Math.floor(champ / 2))

		if (mexLeft < 1) {
			maxLeft = 1
			maxRight = champ
		}

		if (maxRight > pages) {
			maxLeft = pages - (champ - 1)
			maxRight = pages
			if (maxLeft < 1) {
				maxLeft = 1
			}
		}


		for (var page = maxLeft; page <= maxRight; page++) {
			wrapper.innerHTML += `<button value=${page} class="page btn btn-md btn-light">${page}</button>`
		}
		if (numPage != 1) {
			wrapper.innerHTML = `<button value=${1} class="page btn btn-md btn-light">&#171; Début</button>` + wrapper.innerHTML
		}
		if (numPage != pages) {
			wrapper.innerHTML += `<button value=${pages} class="page btn btn-md btn-light">Fin &#187;</button>`
		}

		$('.page').on('click', function () {
			$('#table-div-commande').children(':first-child').empty()
			page = $(this).val()
			buildTable(data, origin, page)
		})
	}

	function buildTable(data, origin, page) {

		var test = paginator(data.result, page, 5)
		var table = $('#table-div-commande').children(':first-child')
		new_content = `<div id='table-div-commande' class="table-wrapper">
				<table id="bootstrap-table" class="table">
					<thead>
					<th  data-field="id" data-visible="false"></th>
					<th  data-field="Commande" data-sortable="true">N° Commande</th>
					<th  data-field="Date" data-sortable="true">Date</th>
					<th  data-field="Client" data-sortable="true">Client</th>
					<th  data-field="Ref" data-sortable="true">Ref Description</th>
					<th  data-field="THT" data-sortable="true">THT</th>
					<th  data-field="TTC" data-sortable="true">TTC</th>
					<th  data-field="Etat" data-sortable="true">Etat</th>
					<th></th>
					<th></th>
					<th></th>
					<th></th>
					<th></th>
				</thead>
					<tbody>`
		for (d in test['result']) {

			new_content = new_content + `<tr>
								<td id = ` + test['result'][d]['id'] + ` hidden></td>
								`
			if (test['result'][d]['n_commande_odoo'] === null) {
				new_content = new_content + `<td></td>`
			} else {
				new_content = new_content + `<td>` + test['result'][d]['n_commande_odoo'] + `</td>`
			}
			new_content = new_content + `
								
								<td>` + test['result'][d]['date'] + `</td>
								<td>` + test['result'][d]['destributeur'] + `</td>
								<td>` + test['result'][d]['reference_description'] + `</td>
								<td>` + intspace(parseFloat(test['result'][d]['totaleHT'])) + `</td>
								<td>` + intspace(parseFloat(test['result'][d]['totaleTTC'])) + `</td>
								<td>` + test['result'][d]['etat'] + `</td>
								<td><button
								  id="` + test['result'][d]['id'] + `"
								  onClick=showDetail(this.id)
								  type="button"
								  class="btn "
								  data-toggle="modal" data-target="#exampleModal"
								>Detail</button></td>

								<td>
								<a
								id="` + test['result'][d]['id'] + `"
								onClick=showDetail(this.id)
								type="button"
								class="btn "
								href="{% url 'pdf_view' com.id %}"
								target="_blank"
							  >Imprimer</a>
							  </td>
							  <td><a
								id="` + test['result'][d]['id'] + `"
							
								type="button"
								`
			if (test['result'][d]['etat'] === 'Annuler' || test['result'][d]['etat'] === 'done') {
				var classB = "btn disabled"
			} else {
				var classB = "btn"
			}
			new_content = new_content +
				`
								class="` +
				classB +


				`
								href="` + origin + "/commerciale/modifier/" + test['result'][d]['id'] + `"
							>Modifier</a></td>
							  <td><button
							  id="` + test['result'][d]['id'] + `"
							  onClick=showDetail(this.id)
							  type="button"
							  `
			if (test['result'][d]['etat'] === 'Annuler' || test['result'][d]['etat'] === 'done') {
				var classB = "btn disabled"
			} else {
				var classB = "btn"
			}
			new_content = new_content +
				`
								class="` +
				classB +

				`
							  data-toggle="modal" data-target="#exampleModal"
							>Modifier</button></td>
							  <td>
								<div class="dropdown">
								  <button `
			if (test['result'][d]['etat'] === 'Annuler' || test['result'][d]['etat'] === 'done') {
				var classB = "btn disabled"
			} else {
				var classB = "btn"
			}
			new_content = new_content + `
								  
								  class="` +
				classB +


				`
								  " type="button" 
								  id="dropdownMenuButton" 
								  data-toggle="dropdown"  
								  aria-expanded="false">
									...
								  </button>
								  <div class="dropdown-menu" aria-labelledby="dropdownMenuButton" disabled>
									<a class="text-danger dropdown-item" href="{% url 'annulerCommande' com.id %}"  style="cursor: default;">Annuler</a>
								  </div>
								</div>
							  </td>
							</tr>`
		}
		new_content = new_content +
			`
						</tbody>
					</table>
				  </div>`
		table.replaceWith(new_content)
		console.log('didnt fet here')
		initiamizeVoutsrapTable()
		console.log('didnt fet here')
		$('#paginator').css('display', 'none')
		pageButtons(test.pages, data, page, 5)
	}

})(jQuery);