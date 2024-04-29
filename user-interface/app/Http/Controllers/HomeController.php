<?php

namespace App\Http\Controllers;

class HomeController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\View\View
     */
    public function index()
    {

        //$output = shell_exec('python3 ~/Network-Monitoring-Security/data-visualization/ResponseTime.py');
        $output ="";
        // Pass the output to the view
        return view('dashboard', ['output' => $output]);
    }
}
