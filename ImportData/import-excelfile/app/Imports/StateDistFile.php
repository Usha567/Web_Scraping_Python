<?php

namespace App\Imports;
use App\Models\State;
use App\Models\District;
use App\Models\Tehsil;
use Illuminate\Support\Collection;
use Maatwebsite\Excel\Concerns\ToCollection;
use Maatwebsite\Excel\Concerns\ToModel;

class StateDistFile implements ToModel
{
    /**
    * @param Collection $collection
    */
    public function model(array $row)
    {
        // echo '$row[0]-'.$row[0];
        // $state=State::create([
        //     'state_name'=>$row[0]!=''?trim($row[0]):NULL,
        // ]);

        // echo '$row[0]-'.$row[0];
        // $state = State::where('state_name', trim($row[0]))->first();
        // if(!is_null($state)){
        //     foreach(explode(',', $row[1]) as $dist){
        //         $district=District::create([
        //             'state_id'=>$state->id,
        //             'district_name'=>trim($dist)
        //         ]);
        //     }
        // }

        echo '$row[0]-'.$row[0];
        $dist = District::where('district_name', trim($row[0]))->first();
        echo 'id--'. $dist->district_name;
        if(!is_null($dist)){
            foreach(explode(',', $row[1]) as $teh){
                echo '$teh- '.$teh;
                $district=Tehsil::create([
                    'district_id'=>$dist->id,
                    'tehsil_name'=>trim($teh)
                ]);
                echo 'dist-- '.$dist;
            }
        }
    }
}
