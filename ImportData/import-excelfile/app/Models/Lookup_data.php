<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Lookup_data extends Model
{
    use HasFactory;
    protected $fillable = ['id','lookup_type_id', 'lookup_data_value'];
}
