# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MyFrame_Rachma
###########################################################################

class MyFrame_Rachma ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hello Wx!", pos = wx.DefaultPosition, size = wx.Size( 1000,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menubar1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		self.m_menubar1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		self.m_menu = wx.Menu()
		self.m_newFile = wx.MenuItem( self.m_menu, wx.ID_ANY, u"New File", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu.Append( self.m_newFile )

		self.m_newProject = wx.MenuItem( self.m_menu, wx.ID_ANY, u"New Project", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu.Append( self.m_newProject )

		self.m_openFile = wx.MenuItem( self.m_menu, wx.ID_ANY, u"Open File", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu.Append( self.m_openFile )

		self.m_openFolder = wx.MenuItem( self.m_menu, wx.ID_ANY, u"Open Folder", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu.Append( self.m_openFolder )

		self.m_exit = wx.MenuItem( self.m_menu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu.Append( self.m_exit )

		self.m_menubar1.Append( self.m_menu, u"Menu" )

		self.m_file = wx.Menu()
		self.m_save = wx.MenuItem( self.m_file, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_file.Append( self.m_save )

		self.m_saveAs = wx.MenuItem( self.m_file, wx.ID_ANY, u"Save As", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_file.Append( self.m_saveAs )

		self.m_print = wx.MenuItem( self.m_file, wx.ID_ANY, u"Print", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_file.Append( self.m_print )

		self.m_menubar1.Append( self.m_file, u"File" )

		self.m_edit = wx.Menu()
		self.m_copy = wx.MenuItem( self.m_edit, wx.ID_ANY, u"Copy", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit.Append( self.m_copy )

		self.m_cut = wx.MenuItem( self.m_edit, wx.ID_ANY, u"Cut", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit.Append( self.m_cut )

		self.m_paste = wx.MenuItem( self.m_edit, wx.ID_ANY, u"Paste", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit.Append( self.m_paste )

		self.m_gambar = wx.MenuItem( self.m_edit, wx.ID_ANY, u"Add Picture", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit.Append( self.m_gambar )

		self.m_Del = wx.MenuItem( self.m_edit, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit.Append( self.m_Del )

		self.m_menubar1.Append( self.m_edit, u"Edit" )

		self.m_tool = wx.Menu()
		self.m_redo = wx.MenuItem( self.m_tool, wx.ID_ANY, u"Redo", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_tool.Append( self.m_redo )

		self.m_undo = wx.MenuItem( self.m_tool, wx.ID_ANY, u"Undo", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_tool.Append( self.m_undo )

		self.m_menubar1.Append( self.m_tool, u"Tool" )

		self.m_help = wx.Menu()
		self.m_about = wx.MenuItem( self.m_help, wx.ID_ANY, u"About Us", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_help.Append( self.m_about )

		self.m_lis = wx.MenuItem( self.m_help, wx.ID_ANY, u"Lisence", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_help.Append( self.m_lis )

		self.m_menubar1.Append( self.m_help, u"Help" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Selamat Datang" ), wx.VERTICAL )

		self.m_myPanel = wx.Panel( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_myPanel.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "Bookman Old Style" ) )
		self.m_myPanel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		self.m_myPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel14 = wx.Panel( self.m_myPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText16 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Nama ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		fgSizer3.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self.m_panel14, wx.ID_ANY, u":  Rachma Ailsya", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		fgSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Nim", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		fgSizer3.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self.m_panel14, wx.ID_ANY, u":  192410101007", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		fgSizer3.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"HELLO WX", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		fgSizer3.Add( self.m_staticText23, 0, wx.ALL, 5 )


		self.m_panel14.SetSizer( fgSizer3 )
		self.m_panel14.Layout()
		fgSizer3.Fit( self.m_panel14 )
		bSizer5.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel15 = wx.Panel( self.m_myPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_animCtrl4 = wx.adv.AnimationCtrl( self.m_panel15, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.adv.AC_DEFAULT_STYLE )
		self.m_animCtrl4.LoadFile( u"D:\\KULIAH\\Pemrograman Berorientasi Object 2\\TUGAS PBO\\Tugas\\tenor_1.gif" )
		bSizer6.Add( self.m_animCtrl4, 0, wx.ALL, 5 )

		self.m_animCtrl5 = wx.adv.AnimationCtrl( self.m_panel15, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.adv.AC_DEFAULT_STYLE )
		self.m_animCtrl5.LoadFile( u"D:\\KULIAH\\Pemrograman Berorientasi Object 2\\TUGAS PBO\\Tugas\\tenor_2.gif" )
		bSizer6.Add( self.m_animCtrl5, 0, wx.ALL, 5 )

		self.m_animCtrl41 = wx.adv.AnimationCtrl( self.m_panel15, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.adv.AC_DEFAULT_STYLE )
		self.m_animCtrl41.LoadFile( u"D:\\KULIAH\\Pemrograman Berorientasi Object 2\\TUGAS PBO\\Tugas\\tenor _5.gif" )
		bSizer6.Add( self.m_animCtrl41, 0, wx.ALL, 5 )

		self.m_animCtrl51 = wx.adv.AnimationCtrl( self.m_panel15, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.adv.AC_DEFAULT_STYLE )
		self.m_animCtrl51.LoadFile( u"D:\\KULIAH\\Pemrograman Berorientasi Object 2\\TUGAS PBO\\Tugas\\tenor_7.gif" )
		bSizer6.Add( self.m_animCtrl51, 0, wx.ALL, 5 )

		self.m_animCtrl6 = wx.adv.AnimationCtrl( self.m_panel15, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.adv.AC_DEFAULT_STYLE )
		self.m_animCtrl6.LoadFile( u"D:\\KULIAH\\Pemrograman Berorientasi Object 2\\TUGAS PBO\\Tugas\\tenor_4.gif" )
		bSizer6.Add( self.m_animCtrl6, 0, wx.ALL, 5 )


		self.m_panel15.SetSizer( bSizer6 )
		self.m_panel15.Layout()
		bSizer6.Fit( self.m_panel15 )
		bSizer5.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.m_myPanel.SetSizer( bSizer2 )
		self.m_myPanel.Layout()
		bSizer2.Fit( self.m_myPanel )
		sbSizer1.Add( self.m_myPanel, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( sbSizer1, 3, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


