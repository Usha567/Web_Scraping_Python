<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Brand_type_mapping extends Model
{
    use HasFactory;
    protected $fillable = ['brand_id', 'product_type_id'];
}
