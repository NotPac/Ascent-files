import uiScriptLocale
import app

window = {
	"name" : "SpecialStorageWindow",

	"x" : SCREEN_WIDTH - 400,
	"y" : 10,

	"style" : ("movable", "float",),

	"width" : 208,
	"height" : 328+32+30,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 208,
			"height" : 328+32+30+8,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 46,
					"y" : 8,

					"width" : 140,
					"color" : "gray",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":84, "y":4, "text":uiScriptLocale.UPGRADE_STORAGE_TITLE, "text_horizontal_align":"center" },
					),
				},

				{
					"name" : "SortButtonImg",
					"type" : "image",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"image" : "d:/ymir work/ui/pattern/titlebar_inv_refresh_baseframe.tga",

					"children" :
					(
						{
							"name" : "SortSpecialButton",
							"type" : "button",

							"x" : 11,
							"y" : 3,

							"default_image" : "d:/ymir work/ui/refresh_small_button_01.sub",
							"over_image" : "d:/ymir work/ui/refresh_small_button_02.sub",
							"down_image" : "d:/ymir work/ui/refresh_small_button_03.sub",
							"disable_image" : "d:/ymir work/ui/refresh_small_button_04.sub",
						},
					),
				},

				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 24,
					"y" : 34,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 9,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
				
				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",

					"x" : 57,
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,

					"children" :
					(
						{
							"name" : "Inventory_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "I",
						},
					),
				},
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",

					"x" : 57 + 32,
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,

					"children" :
					(
						{
							"name" : "Inventory_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "II",
						},
					),
				},

				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",

					"x" : 57 + 32*2,
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_3,

					"children" :
					(
						{
							"name" : "Inventory_Tab_03_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "III",
						},
					),
				},

				{
					"name" : "Category_Tab_01",
					"type" : "radio_button",

					"x" : 14,
					"y" : 295+32+30,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",

					"children" :
					(
						{
							"name" : "Category_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "Upgrades",
						},
					),
				},
					
				{
					"name" : "Category_Tab_02",
					"type" : "radio_button",

					"x" : 14+52,
					"y" : 295+32+30,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",

					"children" :
					(
						{
							"name" : "Category_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "Books",
						},
					),
				},
				
				{
					"name" : "Category_Tab_03",
					"type" : "radio_button",

					"x" : 14+52+52,
					"y" : 295+32+30,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",

					"children" :
					(
						{
							"name" : "Category_Tab_03_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "Stones",
						},
					),
				},
			),
		},
	),
}