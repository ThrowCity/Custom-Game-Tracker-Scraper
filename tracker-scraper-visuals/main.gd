extends Control

var htmlpath : String
var py : Dictionary
var pystd : FileAccess
var pypid : int
var data

### Setup ----------------------------------------------------------------------

func _ready() -> void:
	get_window().connect("files_dropped", _file_dropped)
	if !len(OS.get_cmdline_args()):
		return
	htmlpath = OS.get_cmdline_args()[0]
	print(htmlpath)
	_instantiate_py()
	return

func _instantiate_py():
	if(!FileAccess.file_exists(htmlpath)):
		return
	py = OS.execute_with_pipe("data_manager.exe", [htmlpath])
	pystd = py["stdio"]
	pypid = py["pid"]
	$Initialise.hide()
	$Running.show()
	$Running/ProcessDetails/Path.text = htmlpath
	$Running/ProcessDetails/PID.text = str(pypid)
	$SecondRefresh.start(2)
	return

### File Picking ---------------------------------------------------------------

func _browse_button_pressed() -> void:
	$FilePicker.show()

func _file_chosen(path: String) -> void:
	_file_dropped([path])

func _file_dropped(f : PackedStringArray) -> void:
	htmlpath = f[0]
	_instantiate_py()
	return

### Set Stuff ------------------------------------------------------------------



### Visual Stuff ---------------------------------------------------------------

func _initial_refresh() -> void:
	$Running/ProcessDetails/Heeho/anims.play("breathing_green")
	if OS.is_process_running(pypid):
		$SecondRefresh.start(1)
		$SecondRefresh.disconnect("timeout", _initial_refresh)
		$SecondRefresh.connect("timeout", _second_refreshed)
		var dstr = pystd.get_line()
		print(dstr)
		data = str_to_var(dstr)
		_create_table()
		return
	$Running/ProcessDetails/Heeho.self_modulate = Color.RED
	return

func _second_refreshed() -> void:
	if OS.is_process_running(pypid):
		$SecondRefresh.start(1)
		return
	$Running/ProcessDetails/Heeho.self_modulate = Color.RED
	return

func _create_table() -> void:
	for i in range(len(data)):
		for j in range(len(data[i])):
			get_node("Running/Scoreboard/" + str(i * 14 + j)).text = str(data[i][j])
	return
