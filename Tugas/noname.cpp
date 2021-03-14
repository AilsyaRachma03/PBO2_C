///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame_Rachma::MyFrame_Rachma( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	this->SetForegroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_INACTIVEBORDER ) );
	this->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_ACTIVEBORDER ) );

	m_menubar1 = new wxMenuBar( 0 );
	m_menubar1->SetForegroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_INACTIVECAPTIONTEXT ) );
	m_menubar1->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_GRAYTEXT ) );

	m_menu = new wxMenu();
	wxMenuItem* m_newFile;
	m_newFile = new wxMenuItem( m_menu, wxID_ANY, wxString( wxT("New File") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu->Append( m_newFile );

	wxMenuItem* m_newProject;
	m_newProject = new wxMenuItem( m_menu, wxID_ANY, wxString( wxT("New Project") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu->Append( m_newProject );

	wxMenuItem* m_openFile;
	m_openFile = new wxMenuItem( m_menu, wxID_ANY, wxString( wxT("Open File") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu->Append( m_openFile );

	wxMenuItem* m_openFolder;
	m_openFolder = new wxMenuItem( m_menu, wxID_ANY, wxString( wxT("Open Folder") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu->Append( m_openFolder );

	wxMenuItem* m_exit;
	m_exit = new wxMenuItem( m_menu, wxID_ANY, wxString( wxT("Exit") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu->Append( m_exit );

	m_menubar1->Append( m_menu, wxT("Menu") );

	m_file = new wxMenu();
	wxMenuItem* m_save;
	m_save = new wxMenuItem( m_file, wxID_ANY, wxString( wxT("Save") ) , wxEmptyString, wxITEM_NORMAL );
	m_file->Append( m_save );

	wxMenuItem* m_saveAs;
	m_saveAs = new wxMenuItem( m_file, wxID_ANY, wxString( wxT("Save As") ) , wxEmptyString, wxITEM_NORMAL );
	m_file->Append( m_saveAs );

	wxMenuItem* m_print;
	m_print = new wxMenuItem( m_file, wxID_ANY, wxString( wxT("Print") ) , wxEmptyString, wxITEM_NORMAL );
	m_file->Append( m_print );

	m_menubar1->Append( m_file, wxT("File") );

	m_edit = new wxMenu();
	wxMenuItem* m_copy;
	m_copy = new wxMenuItem( m_edit, wxID_ANY, wxString( wxT("Copy") ) , wxEmptyString, wxITEM_NORMAL );
	m_edit->Append( m_copy );

	wxMenuItem* m_cut;
	m_cut = new wxMenuItem( m_edit, wxID_ANY, wxString( wxT("Cut") ) , wxEmptyString, wxITEM_NORMAL );
	m_edit->Append( m_cut );

	wxMenuItem* m_paste;
	m_paste = new wxMenuItem( m_edit, wxID_ANY, wxString( wxT("Paste") ) , wxEmptyString, wxITEM_NORMAL );
	m_edit->Append( m_paste );

	wxMenuItem* m_gambar;
	m_gambar = new wxMenuItem( m_edit, wxID_ANY, wxString( wxT("Add Picture") ) , wxEmptyString, wxITEM_NORMAL );
	m_edit->Append( m_gambar );

	wxMenuItem* m_Del;
	m_Del = new wxMenuItem( m_edit, wxID_ANY, wxString( wxT("Delete") ) , wxEmptyString, wxITEM_NORMAL );
	m_edit->Append( m_Del );

	m_menubar1->Append( m_edit, wxT("Edit") );

	m_tool = new wxMenu();
	wxMenuItem* m_redo;
	m_redo = new wxMenuItem( m_tool, wxID_ANY, wxString( wxT("Redo") ) , wxEmptyString, wxITEM_NORMAL );
	m_tool->Append( m_redo );

	wxMenuItem* m_undo;
	m_undo = new wxMenuItem( m_tool, wxID_ANY, wxString( wxT("Undo") ) , wxEmptyString, wxITEM_NORMAL );
	m_tool->Append( m_undo );

	m_menubar1->Append( m_tool, wxT("Tool") );

	m_help = new wxMenu();
	wxMenuItem* m_about;
	m_about = new wxMenuItem( m_help, wxID_ANY, wxString( wxT("About Us") ) , wxEmptyString, wxITEM_NORMAL );
	m_help->Append( m_about );

	wxMenuItem* m_lis;
	m_lis = new wxMenuItem( m_help, wxID_ANY, wxString( wxT("Lisence") ) , wxEmptyString, wxITEM_NORMAL );
	m_help->Append( m_lis );

	m_menubar1->Append( m_help, wxT("Help") );

	this->SetMenuBar( m_menubar1 );

	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );

	wxStaticBoxSizer* sbSizer1;
	sbSizer1 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Selamat Datang") ), wxVERTICAL );

	m_myPanel = new wxPanel( sbSizer1->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	m_myPanel->SetFont( wxFont( 12, wxFONTFAMILY_ROMAN, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_LIGHT, false, wxT("Bookman Old Style") ) );
	m_myPanel->SetForegroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_INACTIVECAPTIONTEXT ) );
	m_myPanel->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_3DLIGHT ) );

	wxBoxSizer* bSizer2;
	bSizer2 = new wxBoxSizer( wxVERTICAL );

	wxBoxSizer* bSizer5;
	bSizer5 = new wxBoxSizer( wxVERTICAL );

	m_panel14 = new wxPanel( m_myPanel, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxFlexGridSizer* fgSizer3;
	fgSizer3 = new wxFlexGridSizer( 0, 2, 0, 0 );
	fgSizer3->SetFlexibleDirection( wxBOTH );
	fgSizer3->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );

	m_staticText16 = new wxStaticText( m_panel14, wxID_ANY, wxT("Nama "), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText16->Wrap( -1 );
	fgSizer3->Add( m_staticText16, 0, wxALL, 5 );

	m_staticText17 = new wxStaticText( m_panel14, wxID_ANY, wxT(":  Rachma Ailsya"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText17->Wrap( -1 );
	fgSizer3->Add( m_staticText17, 0, wxALL, 5 );

	m_staticText18 = new wxStaticText( m_panel14, wxID_ANY, wxT("Nim"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText18->Wrap( -1 );
	fgSizer3->Add( m_staticText18, 0, wxALL, 5 );

	m_staticText19 = new wxStaticText( m_panel14, wxID_ANY, wxT(":  192410101007"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText19->Wrap( -1 );
	fgSizer3->Add( m_staticText19, 0, wxALL, 5 );

	m_staticText23 = new wxStaticText( m_panel14, wxID_ANY, wxT("HELLO WX"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText23->Wrap( -1 );
	fgSizer3->Add( m_staticText23, 0, wxALL, 5 );


	m_panel14->SetSizer( fgSizer3 );
	m_panel14->Layout();
	fgSizer3->Fit( m_panel14 );
	bSizer5->Add( m_panel14, 1, wxEXPAND | wxALL, 5 );

	m_panel15 = new wxPanel( m_myPanel, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer6;
	bSizer6 = new wxBoxSizer( wxHORIZONTAL );

	m_animCtrl4 = new wxAnimationCtrl( m_panel15, wxID_ANY, wxNullAnimation, wxDefaultPosition, wxDefaultSize, wxAC_DEFAULT_STYLE );
	m_animCtrl4->LoadFile( wxT("D:\\KULIAH\\Pemrograman Berorientasi Object 2\\TUGAS PBO\\Tugas\\tenor_1.gif") );
	bSizer6->Add( m_animCtrl4, 0, wxALL, 5 );

	m_animCtrl5 = new wxAnimationCtrl( m_panel15, wxID_ANY, wxNullAnimation, wxDefaultPosition, wxDefaultSize, wxAC_DEFAULT_STYLE );
	m_animCtrl5->LoadFile( wxT("D:\\KULIAH\\Pemrograman Berorientasi Object 2\\TUGAS PBO\\Tugas\\tenor_2.gif") );
	bSizer6->Add( m_animCtrl5, 0, wxALL, 5 );

	m_animCtrl41 = new wxAnimationCtrl( m_panel15, wxID_ANY, wxNullAnimation, wxDefaultPosition, wxDefaultSize, wxAC_DEFAULT_STYLE );
	m_animCtrl41->LoadFile( wxT("D:\\KULIAH\\Pemrograman Berorientasi Object 2\\TUGAS PBO\\Tugas\\tenor _5.gif") );
	bSizer6->Add( m_animCtrl41, 0, wxALL, 5 );

	m_animCtrl51 = new wxAnimationCtrl( m_panel15, wxID_ANY, wxNullAnimation, wxDefaultPosition, wxDefaultSize, wxAC_DEFAULT_STYLE );
	m_animCtrl51->LoadFile( wxT("D:\\KULIAH\\Pemrograman Berorientasi Object 2\\TUGAS PBO\\Tugas\\tenor_7.gif") );
	bSizer6->Add( m_animCtrl51, 0, wxALL, 5 );

	m_animCtrl6 = new wxAnimationCtrl( m_panel15, wxID_ANY, wxNullAnimation, wxDefaultPosition, wxDefaultSize, wxAC_DEFAULT_STYLE );
	m_animCtrl6->LoadFile( wxT("D:\\KULIAH\\Pemrograman Berorientasi Object 2\\TUGAS PBO\\Tugas\\tenor_4.gif") );
	bSizer6->Add( m_animCtrl6, 0, wxALL, 5 );


	m_panel15->SetSizer( bSizer6 );
	m_panel15->Layout();
	bSizer6->Fit( m_panel15 );
	bSizer5->Add( m_panel15, 1, wxEXPAND | wxALL, 5 );


	bSizer2->Add( bSizer5, 1, wxEXPAND, 5 );


	m_myPanel->SetSizer( bSizer2 );
	m_myPanel->Layout();
	bSizer2->Fit( m_myPanel );
	sbSizer1->Add( m_myPanel, 1, wxEXPAND | wxALL, 5 );


	bSizer1->Add( sbSizer1, 3, wxEXPAND, 5 );


	this->SetSizer( bSizer1 );
	this->Layout();

	this->Centre( wxBOTH );
}

MyFrame_Rachma::~MyFrame_Rachma()
{
}
