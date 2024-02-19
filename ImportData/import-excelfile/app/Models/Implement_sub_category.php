<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Implement_sub_category extends Model
{
    use HasFactory;
    protected $fillable=['id','implements_category_id','sub_category_name','thumbnail'];
}
