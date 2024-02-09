<?php

namespace App\Imports;
use App\Models\Product;
use App\Models\Brand;
use App\Models\Product_type;
use App\Models\Lookup_data;
use App\Models\Lookup_type;
use App\Models\Accessory;
use App\Models\Accessory_mapping;
use App\Models\Images_mapping;
use App\Models\image_types;
use App\Models\Status_type_mappings;
use App\Models\Status_types;
use Illuminate\Support\Collection;
use Maatwebsite\Excel\Concerns\ToCollection;
use Maatwebsite\Excel\Concerns\ToModel;
use DB;


class TractorDetailsFile implements ToModel
{
    /**
    * @param Collection $collection
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

        // if($row[5] != ''){
        //     $r=explode('+',$row[5]);
        //     $gear_box_forward=explode('Forward', $r[0]);
        //     $gear_box_reverse=explode('Reverse', $r[1]);
        // }
        // else{
        //     $gear_box_forward=[''];
        //     $gear_box_reverse=[''];
        // }

        // echo '$row[0]-'.$row[0];
        // $product = Product::create([
        //     'brand_id'=>$row[0] !=''?Brand::where('brand_name', explode('Tractors',$row[0])[0])->first()->id:NULL,
        //     'product_type_id'=>$row[45] !=''?Product_type::where('product_type_name', $row[45])->first()->id:NULL,
        //     'model'=>$row[1],
        //     'description'=>json_encode($row[9]),
        //     'total_cyclinder_id'=>$row[2]!=''?Lookup_data::where('lookup_data_value', $row[2])->first()->id:NULL,
        //     'hp_category'=>$row[3]!=''?explode('HP', $row[3])[0]:NULL,
        //     'brake_type_id'=>$row[6]!=''?Lookup_data::where('lookup_data_value', $row[6])->first()->id:NULL,
        //     'warranty'=>$row[7],
        //     'starting_price'=>$row[8]!=''?$price[0]:NULL,
        //     'ending_price'=> $row[8]!=''?$price[1]:NULL,
        //     'engine_capacity_cc'=>$row[11]!=''?explode('CC', $row[11])[0]:NULL,
        //     'engine_rated_rpm'=>$row[12],
        //     'cooling_id'=>$row[13]!=''?Lookup_data::where('lookup_data_value', $row[13])->first()->id:NULL,
        //     'air_filter_id'=>$row[14]!=''?Lookup_data::where('lookup_data_value', $row[14])->first()->id:NULL,
        //     'fuel_pump_id'=>$row[15]!=''?Lookup_data::where('lookup_data_value', $row[15])->first()->id:NULL,
        //     'torque'=>$row[16]!=''?explode('NM', $row[16])[0]:NULL,
        //     'transmission_type_id'=>$row[17] !=''?Lookup_data::where('lookup_data_value', $row[17])->first()->id:NULL,
        //     'transmission_clutch_id'=>$row[18]!=''?Lookup_data::where('lookup_data_value', $row[18])->first()->id:NULL,
        //     'gear_box_forward'=>(int) $gear_box_forward[0],
        //     'gear_box_reverse'=>(int) $gear_box_reverse[0],
        //     'min_forward_speed'=> $row[23]!='' &&str_contains($row[23],'-')?explode('-', $row[23])[0]:NULL,
        //     'max_forward_speed'=> $row[23]!=''&& str_contains($row[23],'-')?explode('-', $row[23])[1]:NULL,
        //     'min_reverse_speed'=> $row[25]!=''&& str_contains($row[23],'-')?explode('-', $row[25])[0]:NULL,
        //     'max_reverse_speed'=> $row[25]!=''&& str_contains($row[23],'-')?explode('-', $row[25])[1]:NULL,

        //     'steering_details_id'=> $row[26]!=''?Lookup_data::where('lookup_data_value', $row[26])->first()->id:NULL,
        //     'steering_column_id'=>$row[27]!=''?Lookup_data::where('lookup_data_value', $row[27])->first()->id:NULL,
        //     'power_take_off_type'=>$row[28],
        //     'power_take_off_rpm'=>$row[29],
        //     'total_weight'=>$row[30]!=''?(int)($row[30]):NULL,
        //     'wheel_base'=>$row[31]!=''?(int)$row[31]:NULL,
        //     'lifting_capacity'=>$row[36]!=''?(int)$row[36]:NULL,
        //     'linkage_point_id'=>$row[37]!=''?Lookup_data::where('lookup_data_value', $row[37])->first()->id:NULL,
        //     'wheel_drive_id'=>$row[38]!=''?Lookup_data::where('lookup_data_value',$row[38])->first()->id:NULL,
        //     'front_tyre'=> $row[39],
        //     'rear_tyre'=> $row[40],
        //     'status_id'=>$row[44]!=''?Lookup_data::where('lookup_data_value',$row[44])->first()->id:NULL,
        //     // 'additional_feature'=>$row[42] !=''?$row[42]:NULL
        // ]);

        // if($row[10] !=''){
        //     $statustypemap =  Status_type_mappings::create([
        //         'product_type_id'=>$product->id,
        //         'status_type_id'=>Status_types::where('type_name', $row[10])->first()->id
        //     ]); 
        // }


        // if($row[10] !=''){
        //     $statustypemap =  Status_type_mappings::create([
        //         'product_type_id'=>$product->id,
        //         'status_type_id'=>Status_types::where('type_name', $row[10])->first()->id
        //     ]); 
        // }

        // if($row[41] !=''){
        //     $accessories =  Accessory_mapping::create([
        //         'product_id'=>$product->id,
        //         'accessory_id'=>Accessory::where('accessory', $row[41])->first()->id
        //     ]);
        // }

        #Need to play with image here
        echo '$row[1]-'.$row[1];
        $prod = Product::where('model', $row[1])->first();
        if(!is_null($prod)){
            $prod_id= $prod->id;
            foreach(explode(',', $row[2]) as $p){
                $imagemapping = Images_mapping::create([
                    'product_id'=>  $prod_id,
                    'image_type_id'=>image_types::where('image_type_name', trim($row[3]))->first()->id,
                    'image_name'=>trim($p)
                ]);
            }
        }
        else{
            echo 'prod null';
        }
       
    }
}
