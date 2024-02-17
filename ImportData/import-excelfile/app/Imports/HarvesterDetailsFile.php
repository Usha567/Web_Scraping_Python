<?php

namespace App\Imports;

use App\Models\Product;
use App\Models\Brand;
use App\Models\Product_type;
use App\Models\Lookup_data;
use App\Models\Lookup_type;
use App\Models\Images_mapping;
use App\Models\image_types;
use Maatwebsite\Excel\Concerns\ToModel;

class HarvesterDetailsFile implements ToModel
{
    /**
    * @param array $row
    *
    * @return \Illuminate\Database\Eloquent\Model|null
    */
    public function model(array $row)
    {
        //For checking error
        // echo '$row[10]-'.$row[10] . "\n";
        // if($row[10]!=''){
        //     $id=Status_types::where('type_name', $row[10])->first()->id;
        //     echo 'id-'.$id;
        // }
        // else{
        //     echo 'else\n';
        //     null;
        // }

        // echo '$row[29]-'.$row[29];
        // if($row[29] != ''){
        //     $r=explode('+',$row[29]);
        //     $gear_box_forward=$r[0];
        //     $gear_box_reverse=$r[1];
        // }
        // else{
        //     $gear_box_forward=[''];
        //     $gear_box_reverse=[''];
        // }

        echo 'harvester model-'.$row[1] ;
        $prod = Product::where('model', $row[1])->first();
        if(!is_null($prod)){
            echo 'id-'.$prod->id;

            $prod->brand_id=$row[0]!=''?Brand::where('brand_name', trim($row[0]))->first()->id:NULL;
            $prod->product_type_id=$row[40] !=''?Product_type::where('product_type_name', trim($row[40]))->first()->id:NULL;
            $prod->model=trim($row[1]);
            $prod->total_cyclinder_id=$row[4]!=''?Lookup_data::where('lookup_data_value', trim($row[4]))->first()->id:NULL;
            $prod->hp_category=$row[9]!=''?trim($row[9]):NULL;
            $prod->engine_rated_rpm=trim($row[8]);
            $prod->air_filter_id=$row[11]!=''?Lookup_data::where('lookup_data_value', trim($row[11]))->first()->id:NULL;
            $prod->power_source_id=$row[5]!=''?Lookup_data::where('lookup_data_value', trim($row[5]))->first()->id:NULL;
        
            $prod->cutting_bar_width=$row[3]!=''?trim($row[3]):NULL;
            $prod->min_cutting_height=$row[12]!=''?trim($row[12]):NULL;
            $prod->max_cutting_height=$row[13]!=''?trim($row[13]):NULL;
            $prod->cutter_bar_height_adjustment_id=$row[14]!=''?Lookup_data::where('lookup_data_value', trim($row[14]))->first()->id:NULL;
            $prod->reel_type_id=$row[15]!=''?Lookup_data::where('lookup_data_value', trim($row[15]))->first()->id:NULL;
            $prod->reel_diameter=$row[16]!=''?trim($row[16]):NULL;
            $prod->speed_adjustment_id=$row[17]!=''?Lookup_data::where('lookup_data_value', trim($row[17]))->first()->id:NULL;
            $prod->reel_height_adjustment_id=$row[20]!=''?Lookup_data::where('lookup_data_value', trim($row[20]))->first()->id:NULL;
            $prod->min_reel_revolution=$row[19]!=''?trim($row[19]):NULL;
            $prod->max_reel_revolution=$row[18]!=''?trim($row[18]):NULL;
            $prod->cooling_id=$row[21]!=''?Lookup_data::where('lookup_data_value', trim($row[21]))->first()->id:NULL;
            $prod->coolant_capacity=$row[22]!=''?trim($row[22]):NULL;

            $prod->threshing_drum_width=$row[23]!=''?trim($row[23]):NULL;
            $prod->threshing_drum_length=$row[24]!=''?trim($row[24]):NULL;
            $prod->threshing_drum_diameter=$row[25]!=''?trim($row[25]):NULL;
            $prod->threshing_drum_speed_adjustment_id=$row[26]!=''?Lookup_data::where('lookup_data_value', trim($row[26]))->first()->id:NULL;
            $prod->clearance_concave=$row[27]!=''?trim($row[27]):NULL;

            $prod->grain_tank_capacity=$row[28]!=''?trim($row[28]):NULL;
            $prod->transmission_forward =$gear_box_forward;
            $prod->transmission_reverse=$gear_box_reverse;
            $prod->clutch_type_id= $row[30]!=''?Lookup_data::where('lookup_data_value', trim($row[30]))->first()->id:NULL;
            $prod->front_tyre= $row[31]!=''?trim($row[31]):NULL;
            $prod->rear_tyre= $row[32]!=''?trim($row[32]):NULL;
            $prod->total_weight_without_grains= $row[34]!=''?trim($row[34]):NULL;
            $prod->dimension_length= $row[35]!=''?trim($row[35]):NULL;
            $prod->dimension_width=$row[36]!=''?trim($row[36]):NULL;
            $prod->dimension_height=$row[37]!=''?trim($row[37]):NULL;
            $prod->ground_clearance=$row[38]!=''?trim($row[38]):NULL;
            $prod->crops_type_id=$row[6]!=''?Lookup_data::where('lookup_data_value',trim($row[6]))->first()->id:NULL;
            // $imagemapping = Images_mapping::create([
            //     'product_id'=>  $prod->id,
            //     'image_type_id'=>image_types::where('image_type_name', trim($row[39]))->first()->id,
            //     'image_name'=>trim($row[2])
            // ]);
            $prod->save();
        }
        
        
        #Need to play with image here
        // echo '$row[1]-'.$row[1];
        // $prod = Product::where('model', $row[1])->first();
        // if(!is_null($prod)){
        //     $prod_id= $prod->id;
        //     $imgmaps=Images_mapping::where('product_id',  $prod_id)->get();
        //         if(!is_null($imgmaps)){
        //             foreach($imgmaps as $imgd){
        //                 $imgd->delete();
        //             }
        //     }
        //     // $imagemapping = Images_mapping::create([
        //     //     'product_id'=>  $prod_id,
        //     //     'image_type_id'=>image_types::where('image_type_name', trim($row[39]))->first()->id,
        //     //     'image_name'=>trim($row[2])
        //     // ]);
        // }
        // else{
        //     echo 'prod null';
        // }
    }
}
