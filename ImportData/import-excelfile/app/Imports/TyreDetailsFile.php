<?php

namespace App\Imports;

use App\Models\Product;
use App\Models\Tyre;
use App\Models\Brand;
use App\Models\Product_type;
use App\Models\Tyre_category;
use App\Models\Lookup_data;
use App\Models\Lookup_type;
use App\Models\Images_mapping;
use App\Models\image_types;
use Maatwebsite\Excel\Concerns\ToModel;

class TyreDetailsFile implements ToModel
{
    /**
    * @param array $row
    *
    * @return \Illuminate\Database\Eloquent\Model|null
    */
    public function model(array $row)
    {
        // echo '$row[5]-'.$row[5];
        // if($row[5]!='' && $row[6]==''){
        //     $tyre_size=trim($row[5]);
        // }
        // else if ($row[5]=='' && $row[6]!=''){
        //     $tyre_size=trim($row[6]);
        // }
        // else if($row[5]!='' && $row[6]!=''){
        //     $tyre_size=$row[5].'X'.trim($row[6]);
        // }
        // else if ($row[5]=='' && $row[6]==''){
        //     $tyre_size=NULL;
        // }
        // // To update data
        // $tyre = Tyre::where('model', $row[1])->first();
        // if(!is_null($tyre)){
        //     $tyre->brand_id=$row[0]!=''?Brand::where('brand_name', trim($row[0]))->first()->id:NULL;
        //     $tyre->tyre_model=$row[1];
        //     $tyre->tyre_category_id=$row[3]!=''?Tyre_category::where('category', trim($row[3]))->first()->id:NULL;
        //     $tyre->tyre_position=$row[4]!=''?trim($row[4]):NULL;
        //     $tyre->tyre_size=$tyre_size;
        
        //     // To delete data
        //     // $tyre->delete();
        //     // $imgmaps=Images_mapping::where('product_id',  $tyre->id)->get();
        //     // if(!is_null($imgmaps)){
        //     //     foreach($imgmaps as $imgd){
        //     //         $imgd->delete();
        //     //     }
        //     // }
        //     foreach(explode(',', $row[2]) as $p){
        //         $imagemapping = Images_mapping::create([
        //             'product_id'=>  $tyre->id,
        //             'image_type_id'=>image_types::where('image_type_name', trim($row[8]))->first()->id,
        //             'image_name'=>trim($p)
        //         ]);
        //     }
        // }

        // $tyre=Tyre::create([
        //     'brand_id'=>$row[0]!=''?Brand::where('brand_name', trim($row[0]))->first()->id:NULL,
        //     'tyre_model'=>$row[1],
        //     'tyre_category_id'=>$row[3]!=''?Tyre_category::where('category', trim($row[3]))->first()->id:NULL,
        //     'tyre_position'=>$row[4]!=''?trim($row[4]):NULL,
        //     'tyre_size'=>$tyre_size,
        // ]);
        // $tyre->save();
        
        #Need to play with image here
        echo '$row[1]-'.$row[1];
        $tyres = Tyre::where('tyre_model', $row[1])->get();
        if(!is_null($tyres)){
            foreach($tyres as $tyre){
                $tyre_id= $tyre->id;
                echo' $tyre_id---'. $tyre_id;
                // $tyre->delete();
                // $imgmaps=Images_mapping::where('product_id',  $tyre->id)->get();
                // if(!is_null($imgmaps)){
                //     foreach($imgmaps as $imgd){
                //         $imgd->delete();
                //     }
                // }
            
                // foreach(explode(',', $row[2]) as $p){
                    $imagemapping = Images_mapping::create([
                        'product_id'=>  $tyre_id,
                        'image_type_id'=>image_types::where('image_type_name', trim($row[8]))->first()->id,
                        'image_name'=>trim($row[2])
                    ]);
                // }
            }
        }
        else{
            echo 'tyre null';
        }
    }
}
