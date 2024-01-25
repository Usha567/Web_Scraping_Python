<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Images_mapping extends Model
{
    use HasFactory;
    protected $fillable =['id','product_id', 'image_type_id','image_name'];
}
