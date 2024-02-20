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
use App\Models\Implement_category;
use App\Models\Implement_sub_category;
use Illuminate\Support\Collection;
use Maatwebsite\Excel\Concerns\ToCollection;
use Maatwebsite\Excel\Concerns\ToModel;

class FarmImplementFile implements ToModel
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

        echo 'Farm-Implement $row[0]-'.$row[1];
        // $sub_cat_id = Implement_sub_category::where('sub_category_name',trim($row[3]))->first()->id;
        // echo 'subcatid-- '.$sub_cat_id;

        $products = Product::where('model', trim($row[1]))->first();
        // // echo 'here--'.$products->id;
        if(!is_null($products)){
            echo 'here--'.$products->id;
        //     // //'implement_category_id'=>$row[2]!=''?Implement_category::where('category_name',trim($row[2]))->first()->id:NULL,
        //     //$products->implement_sub_category_id=$row[3]!=''?Implement_sub_category::where('sub_category_name',trim($row[3]))->first()->id:NULL;
            $products->implement_sub_category_id=$row[3]!=''?Implement_sub_category::where('sub_category_name',trim($row[3]))->first()->id:NULL;
            $products->CUSTOM_1=$row[61];
            $products->CUSTOM_2=$row[64];
            $products->CUSTOM_3=$row[63];
            $products->CUSTOM_4=$row[65];
            $products->CUSTOM_5=$row[66];
            $products->CUSTOM_6=$row[67];
            $products->CUSTOM_7=$row[10];
            $products->CUSTOM_8=$row[68];
            $products->CUSTOM_9=$row[69];
            $products->CUSTOM_10=$row[70];
            $products->CUSTOM_11=$row[71];

            // $products->CUSTOM_12=$row[31];
            // $products->CUSTOM_13=$row[51];
            // $products->CUSTOM_14=$row[52];
            // $products->CUSTOM_15=$row[14];
            // $products->CUSTOM_16=$row[53];
            // $products->CUSTOM_17=$row[31];
            // $products->CUSTOM_18=$row[31];
            // $products->CUSTOM_19=$row[27];
            // $products->CUSTOM_20=$row[32];
            // $products->CUSTOM_21=$row[33];
            // $products->CUSTOM_22=$row[34];
            // $products->CUSTOM_23=$row[35];
            // $products->CUSTOM_24=$row[36];
            // $products->CUSTOM_25=$row[37];
            $products->save();
        }
      

        // $product = Product::create([
        //     'brand_id'=>$row[0] !=''?Brand::where('brand_name', trim($row[0]))->first()->id:NULL,
        //     'product_type_id'=>$row[38] !=''?Product_type::where('product_type_name', trim($row[38]))->first()->id:NULL,
        //     'model'=>$row[1],
        //     'implement_category_id'=>$row[2]!=''?Implement_category::where('category_name',trim($row[2]))->first()->id:NULL,
            // 'implement_sub_category_id'=>$row[3]!=''?Implement_sub_category::where('sub_category_name',trim($row[3]))->first()->id:NULL,
            // 'CUSTOM_1'=>$row[31],
            // 'CUSTOM_2'=>$row[6],
            // 'CUSTOM_3'=>$row[7],
            // 'CUSTOM_4'=>$row[8],
            // 'CUSTOM_5'=>$row[9],
            // 'CUSTOM_6'=>$row[10],
            // 'CUSTOM_7'=>$row[11],
            // 'CUSTOM_8'=>$row[12],
            // 'CUSTOM_9'=>$row[13],
            // 'CUSTOM_10'=>$row[14],
            // 'CUSTOM_11'=>$row[15],
            // 'CUSTOM_12'=>$row[16],
            // 'CUSTOM_13'=>$row[17],
            // 'CUSTOM_14'=>$row[18],
            // 'CUSTOM_15'=>$row[19],
            // 'CUSTOM_16'=>$row[20],
            // 'CUSTOM_17'=>$row[21],
            // 'CUSTOM_18'=>$row[22],
            // 'CUSTOM_19'=>$row[23],
            // 'CUSTOM_20'=>$row[24],
            // 'CUSTOM_21'=>$row[25],
            // 'CUSTOM_22'=>$row[26],
            // 'CUSTOM_23'=>$row[27],
            // 'CUSTOM_24'=>$row[28],
            // 'CUSTOM_25'=>$row[29],
            // 'CUSTOM_26'=>$sub_cat_id==1?$row[31]:NULL,
        // ]);
        // $product->save();

        #Need to play with image here
        // $prods = Product::where('model', ($row[1]))->get();
        // if(!is_null($prods)){
        //     foreach($prods as $prod){
        //         $prod_id= $prod->id;
        //         'id- '.$prod_id;
        //         // $imgmaps=Images_mapping::where('product_id',  $prod->id)->get();
        //         // if(!is_null($imgmaps)){
        //         //     foreach($imgmaps as $imgd){
        //         //         $imgd->delete();
        //         //     }
        //         // }
        //         foreach(explode(',', $row[4]) as $p){
        //             $imagemapping = Images_mapping::create([
        //                 'product_id'=>  $prod_id,
        //                 'image_type_id'=>image_types::where('image_type_name', trim($row[5]))->first()->id,
        //                 'image_name'=>trim($p)
        //             ]);
        //         }
        //     }
        // }
        // else{
        //     echo 'prod null';
        // }
    }
}
